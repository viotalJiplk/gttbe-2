from ..utils import dbConn
import datetime
import requests
from ..utils import config, fetchAllWithNames
from requests import post
from datetime import date, datetime, timedelta
import json
from ..utils import ObjectDbSync
from typing import Union

class UserModel(ObjectDbSync):
    """Represents user

    Attributes:
        userId (int): id of user
        name (Union[str, None]): name of the user
        surname (Union[str, None]): surname of user
        adult (Union[bool, None]): is user adult
        schoolId (Union[int, None]): id of school user belongs to

    """
    tableName = "users"
    tableId = "userId"

    def __init__(self, userId: Union[int, None] = None, refresh_token: Union[str, None] = None, access_token: Union[str, None] = None, expires_in: Union[str, datetime, None] = None, surname: Union[str, None] = None,  name: Union[str, None] = None, adult: Union[bool, None] = None, schoolId: Union[int, None] = None, camera: bool = False):
        """Initializes user representation

        Args:
            userId ( Union[int, None]): id of user. Defaults to None.
            refresh_token (Union[str, None], optional): users refresh token. Defaults to None.
            access_token (Union[str, None], optional): users access token. Defaults to None.
            expires_in (Union[str, datetime, None], optional): time when token expires. Defaults to None.
            name (Union[str, None], optional): name of the user. Defaults to None.
            surname (Union[str, None], optional): surname of user. Defaults to None.
            adult (Union[bool, None], optional): is user adult. Defaults to None.
            schoolId (Union[int, None], optional): id of school user belongs to. Defaults to None.
        """
        if(not isinstance(expires_in, datetime) and expires_in is not None):
            expires_in = datetime.utcfromtimestamp(expires_in)
        self.userId = userId
        self.surname = surname
        self.name = name
        if adult is not None:
            self.adult = bool(adult)
        else:
            self.adult = None
        self.schoolId = schoolId
        self.camera = bool(camera)
        self.__access_token = access_token
        self.__refresh_token = refresh_token
        self.__expires_in = expires_in
        super().__init__()

    def __str__(self):
        return json.dumps(self.toDict())

    def toDict(self):
        """Returns dict representation of object.

        Returns:
            dict: dict representation of object
        """
        discordUserObject = None
        try:
            discordUserObject = self.getDiscordUserObject()
        except Exception as e:
            pass
        return {
            "userId": self.userId,
            "surname": self.surname,
            "name": self.name,
            "adult": self.adult,
            "camera": self.camera,
            "schoolId": self.schoolId,
            "discord_user_object": discordUserObject
        }

    @classmethod
    @dbConn(autocommit=True, buffered=True)
    def updateOrCreateUser(cls, cursor, db, userId: Union[int, None], refresh_token: Union[str, None] = None, access_token: Union[str, None] = None, expires_in: Union[str, datetime, None] = None, name: Union[str, None] = None, surname: Union[str, None]  = None, adult: Union[bool, None]  = None, schoolId: Union[int, None]  = None, camera: bool = False):
        """Update or create user (useful for logging in/registration)

        Args:
            userId ( Union[int, None]): id of user. Defaults to None.
            refresh_token (Union[str, None], optional): users refresh token. Defaults to None.
            access_token (Union[str, None], optional): users access token. Defaults to None.
            expires_in (Union[str, None], optional): time when token expires. Defaults to None.
            name (Union[str, None], optional): name of the user. Defaults to None.
            surname (Union[str, None], optional): surname of user. Defaults to None.
            adult (Union[bool, None], optional): is user adult. Defaults to None.
            schoolId (Union[int, None], optional): id of school user belongs to. Defaults to None.

        Raises:
            Exception: Missing userId.
            Exception: Missing something in request or there is nothing to update.

        Returns:
            UserModel: new or updated userModel
        """

        if(userId is None):
                raise Exception("Missing userId.")

        values = {
            'userId': userId,
        }

        # try if user already exists
        query = "UPDATE users SET"

        if(refresh_token is not None):
            values["refresh_token"] = refresh_token
        if(access_token is not None):
            values["access_token"] = access_token
        if(expires_in is not None):
            values["expires_in"] = expires_in
        if(name is not None):
            values["name"] = name
        if(surname is not None):
            values["surname"] = surname
        if(adult is not None):
            values["adult"] = adult
        if(schoolId is not None):
            values["schoolId"] = schoolId

        first = True
        for toSet in values:
            if not first:
                query += ","
            else:
                first = False
            query += " `" + toSet +  "` = %(" + toSet + ")s"

        query += " WHERE `userId` = %(userId)s;"

        cursor.execute(query, values)
        if(cursor.rowcount != 1):
            # user does not exist yet
            if(refresh_token == '' or access_token == '' or expires_in == ''):
                raise Exception("Missing something in request or there is nothing to update.")
            query_start = "INSERT INTO users ("
            query_end = ") VALUES ("
            first = True
            for toSet in values:
                if not first:
                    query_start += ","
                    query_end += ","
                else:
                    first = False
                query_start += " `" + toSet +  "`"
                query_end += "%(" + toSet + ")s"
            cursor.execute(query_start + query_end + ");", values)

        return cls(userId=userId, refresh_token=refresh_token, access_token=access_token, expires_in=expires_in, name=name, surname=surname, adult=adult, schoolId=schoolId, camera=camera)

    @classmethod
    def getByCode(cls, code: str, redirect_uri: str, name: Union[str, None], surname: Union[str, None], adult: Union[bool, None], schoolId: Union[int, None], camera: bool = False):
        """Exchange code for access and refresh tokens

        Args:
            code (str): Oauth authorization code
            redirect_uri (str): uri that te user was redirected to
            name (Union[str, None]): name of the user
            surname (Union[str, None]): surname of the user
            adult (Union[bool, None]): is user adult
            schoolId (Union[int, None]): id of users shool

        Returns:
            UserModel: user
        """
        data = {
            'client_id': config.discord.client_id,
            'client_secret': config.discord.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        tokenReq = UserModel.tokenEndpoint(data)

        ''' now lets get discords user object'''
        user = UserModel(access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"])
        userObject = user.getDiscordUserObject()

        return (UserModel.updateOrCreateUser(userId = userObject["id"], refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"], name=name, surname=surname, adult=adult, schoolId=schoolId, camera=camera), userObject)

    def getDiscordUserObject(self):
        """Returns this user discord info

        Raises:
            Exception: discord /oauth2/@me error:
            Exception: discord /oauth2/@me responded:

        Returns:
            dict: user discord info
        """
        today = datetime.today()
        if(self.__expires_in < today):
            self.__refresh_token_refresh()
        try:
            headers = {
                "Authorization": "Bearer " + self.__access_token
            }
            userObjectReq = requests.get('%s/oauth2/@me' % config.discord.api_endpoint, headers=headers)
        except Exception as e:
            raise Exception("discord /oauth2/@me error: " + e.args[0])
            #discord token endpoint error
        if(userObjectReq.status_code != 200):
            raise Exception("discord /oauth2/@me responded: " + str(userObjectReq.status_code) + userObjectReq.text)
            #discord token endpoint error
        userObjectReq = userObjectReq.json()
        return userObjectReq['user']

    @classmethod
    def tokenEndpoint(cls, data: dict):
        """Post data to token endpoint

        Args:
            data (dict): data to send

        Raises:
            Exception: discord token endpoint error:
            Exception: discord token endpoint responded:
            Exception: discord token endpoint response missing token type
            Exception: discord token endpoint response unknown token type
            Exception: discord token endpoint response missing access_token
            Exception: discord token endpoint response missing refresh_token
            Exception: discord token endpoint response missing expires_in

        Returns:
            dict: response
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            tokenReq = post('%s/oauth2/token' % config.discord.api_endpoint, data=data, headers=headers)
        except Exception as e:
            raise Exception("discord token endpoint error: "  + e.args[0])
            #discord token endpoint error
        if(tokenReq.status_code != 200):
            raise Exception("discord token endpoint responded: " + str(tokenReq.status_code) + tokenReq.text)
            #discord token endpoint error
        tokenReq = tokenReq.json()

        if("token_type" not in tokenReq):
            raise Exception("discord token endpoint response missing token type")
        if(tokenReq["token_type"] != "Bearer"):
            raise Exception("discord token endpoint response unknown token type")
        if("access_token" not in tokenReq):
            raise Exception("discord token endpoint response missing access_token")
        if("refresh_token" not in tokenReq):
            raise Exception("discord token endpoint response missing refresh_token")
        if("expires_in" not in tokenReq):
            raise Exception("discord token endpoint response missing expires_in")

        tokenReq["expires_in"] = datetime.now() + timedelta(0, tokenReq["expires_in"])
        return tokenReq

    def __refresh_token_refresh(self):
        data = {
            'client_id': config.discord.client_id,
            'client_secret': config.discord.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token
        }
        tokenReq = UserModel.tokenEndpoint(data)

        UserModel.updateOrCreateUser(userId = self.userId, refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"])

        self.__refresh_token = tokenReq["refresh_token"]
        self.__access_token = tokenReq["access_token"]
        self.__expires_in = tokenReq["expires_in"]

        return self

    def canRegister(self):
        """Test if user can register

        Returns:
            boolean: can user register
        """
        return ((self.userId != "") and (self.surname != "") and (self.name != "") and (self.adult != None) and (self.schoolId != None ))

    @dbConn()
    def listPermissions(self, gameId: Union[str, None, True], cursor, db):
        """List users permission

        Args:
            gameId (Union[str, None]): str with gameId (specific game), None (only for all games), True for all games

        Returns:
            list[dict]: list of teams
        """
        if gameId is None:
            query = """SELECT p.permission, arp.gameId FROM users u
JOIN userRoles ur ON u.userId = ur.userId
JOIN assignedRoles ar ON ur.assignedRoleId = ar.assignedRoleId
JOIN assignedRolePermissions arp ON ar.assignedRoleId = arp.assignedRoleId
JOIN permissions p ON arp.permission = p.permission
WHERE u.userId = %(userId)s AND arp.gameId is NULL
UNION
SELECT p.permission, arp.gameId FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public', 'user')
) AND arp.gameId is NULL
UNION
SELECT generatedRolePermissions.permission AS permission, generatedRolePermissions.gameId AS gameId FROM `registrations`
JOIN generatedRoles ON generatedRoles.generatedRoleId = registrations.generatedRoleID
JOIN generatedRolePermissions ON generatedRolePermissions.generatedRoleID =  generatedRoles.generatedRoleId
JOIN teams ON registrations.teamId = teams.teamId
WHERE `userId` = %(userId)s AND ((teams.canPlaySince IS NOT NULL and generatedRolePermissions.eligible = 1)
OR (teams.canPlaySince IS NULL and generatedRolePermissions.eligible = 0)) AND generatedRoles.gameId IS NULL"""
            cursor.execute(query,  {'userId': self.userId})
        elif gameId == True:
            query = """SELECT p.permission, arp.gameId FROM users u
JOIN userRoles ur ON u.userId = ur.userId
JOIN assignedRoles ar ON ur.assignedRoleId = ar.assignedRoleId
JOIN assignedRolePermissions arp ON ar.assignedRoleId = arp.assignedRoleId
JOIN permissions p ON arp.permission = p.permission
WHERE u.userId = %(userId)s
UNION
SELECT p.permission, arp.gameId FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public', 'user')
)
UNION
SELECT generatedRolePermissions.permission AS permission, generatedRolePermissions.gameId AS gameId FROM `registrations`
JOIN generatedRoles ON generatedRoles.generatedRoleId = registrations.generatedRoleID
JOIN generatedRolePermissions ON generatedRolePermissions.generatedRoleID =  generatedRoles.generatedRoleId
JOIN teams ON registrations.teamId = teams.teamId
WHERE `userId` = %(userId)s AND ((teams.canPlaySince IS NOT NULL and generatedRolePermissions.eligible = 1)
OR (teams.canPlaySince IS NULL and generatedRolePermissions.eligible = 0))"""
            cursor.execute(query,  {'userId': self.userId})
        else:
            query = """SELECT p.permission, arp.gameId FROM users u
JOIN userRoles ur ON u.userId = ur.userId
JOIN assignedRoles ar ON ur.assignedRoleId = ar.assignedRoleId
JOIN assignedRolePermissions arp ON ar.assignedRoleId = arp.assignedRoleId
JOIN permissions p ON arp.permission = p.permission
WHERE u.userId = %(userId)s AND (arp.gameId is NULL OR arp.gameId = %(gameId)s)
UNION
SELECT p.permission, arp.gameId FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public', 'user')
) AND (arp.gameId is NULL OR arp.gameId = %(gameId)s)
UNION
SELECT generatedRolePermissions.permission AS permission, generatedRolePermissions.gameId AS gameId FROM `registrations`
JOIN generatedRoles ON generatedRoles.generatedRoleId = registrations.generatedRoleID
JOIN generatedRolePermissions ON generatedRolePermissions.generatedRoleID =  generatedRoles.generatedRoleId
JOIN teams ON registrations.teamId = teams.teamId
WHERE `userId` = %(userId)s AND ((teams.canPlaySince IS NOT NULL and generatedRolePermissions.eligible = 1)
OR (teams.canPlaySince IS NULL and generatedRolePermissions.eligible = 0)) AND (generatedRoles.gameId IS NULL OR generatedRoles.gameId = %(gameId)s)"""
            cursor.execute(query, {'userId': self.userId, 'gameId': gameId})
        return fetchAllWithNames(cursor)

    @dbConn()
    def listGeneratedRoles(self, cursor, db):
        """List users generatedRoles

        Returns:
            list[dict]: list of generatedRoles
        """
        query = """ SELECT r.teamId, g.* FROM users AS u
                    RIGHT JOIN registrations AS r ON u.userId = r.userId
                    RIGHT JOIN generatedRoles AS g ON g.generatedRoleId = r.generatedRoleId
                    WHERE u.userId = %(userId)s
        """
        cursor.execute(query,  {'userId': self.userId})
        return fetchAllWithNames(cursor)

    @dbConn()
    def listAssignedRoles(self, cursor, db):
        """List users assignedRoles

        Returns:
            list[dict]: list of assignedRoles
        """
        query = """
            SELECT ar.* FROM assignedRoles AS ar
            RIGHT JOIN userRoles as ur ON ur.assignedRoleId = ar.assignedRoleId
            WHERE ar.roleName IN ("user", "public") OR userId=%(userId)s
        """
        cursor.execute(query,  {'userId': self.userId})
        return fetchAllWithNames(cursor)
