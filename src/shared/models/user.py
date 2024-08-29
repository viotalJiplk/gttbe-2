from ..utils import dbConn
import datetime
import requests
from ..utils import config
from requests import post
from datetime import date, datetime, timedelta
import json
from ..utils import ObjectDbSync
from typing import Union

class UserModel(ObjectDbSync):
    tableName = "users"
    tableId = "userId"

    def __init__(self, userId = '', refresh_token = '', access_token = '', expires_in = '', name='', surname='', adult='', schoolId=''):
        if(not isinstance(expires_in, datetime) and expires_in != ''):
            expires_in = datetime.utcfromtimestamp(expires_in)
        self.userId = userId
        self.surname = surname
        self.name = name
        self.adult = adult
        self.schoolId = schoolId
        self.__access_token = access_token
        self.__refresh_token = refresh_token
        self.__expires_in = expires_in
        super().__init__()

    def __str__(self):
        return json.dumps(self.toDict())

    def toDict(self):
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
            "schoolId": self.schoolId,
            "discord_user_object": discordUserObject
        }

    @classmethod
    @dbConn(autocommit=True, buffered=True)
    def updateOrCreateUser(cls, cursor, db, userId = '', refresh_token = '', access_token = '', expires_in = '', name='', surname='', adult='', schoolId=''):
        if(userId == ''):
                raise Exception("Missing userid.")

        values = {
            'userId': userId,
        }

        # try if user already exists
        query = "UPDATE users SET"

        if(refresh_token != ''):
            values["refresh_token"] = refresh_token
        if(access_token != ''):
            values["access_token"] = access_token
        if(expires_in != ''):
            values["expires_in"] = expires_in
        if(name != ''):
            values["name"] = name
        if(surname != ''):
            values["surname"] = surname
        if(adult != ''):
            values["adult"] = adult
        if(schoolId != ''):
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

        return cls(userId=userId, refresh_token=refresh_token, access_token=access_token, expires_in=expires_in, name=name, surname=surname, adult=adult, schoolId=schoolId)

    @classmethod
    def getByCode(cls, code, redirect_uri, name, surname, adult, schoolId):
        '''exchange code for access and refresh tokens'''
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

        return (UserModel.updateOrCreateUser(userId = userObject["id"], refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"], name=name, surname=surname, adult=adult, schoolId=schoolId), userObject)

    def getDiscordUserObject(self):
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
    def tokenEndpoint(cls, data):

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
        return ((self.userId != "") and (self.surname != "") and (self.name != "") and (self.adult != None) and (self.schoolId != None ))

    @dbConn()
    def listPermissions(self, gameId: Union[str, None], cursor, db):
        if gameId is None:
            query = """SELECT p.permission FROM users u
JOIN userRoles ur ON u.userId = ur.userId
JOIN assignedRoles ar ON ur.assignedRoleId = ar.assignedRoleId
JOIN assignedRolePermissions arp ON ar.assignedRoleId = arp.assignedRoleId
JOIN permissions p ON arp.permission = p.permission
WHERE u.userId = %(userId)s AND arp.gameId is NULL
UNION
SELECT p.permission FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public', 'user')
) AND arp.gameId is NULL
UNION
SELECT generatedRolePermissions.permission AS permission FROM `registrations`
JOIN generatedRoles ON generatedRoles.generatedRoleId = registrations.generatedRoleID
JOIN generatedRolePermissions ON generatedRolePermissions.generatedRoleID =  generatedRoles.generatedRoleId
JOIN teams ON registrations.teamId = teams.teamId
WHERE `userId` = %(userId)s AND ((teams.canPlaySince IS NOT NULL and generatedRolePermissions.eligible = 1)
OR (teams.canPlaySince IS NULL and generatedRolePermissions.eligible = 0)) AND generatedRoles.gameId IS NULL"""
            cursor.execute(query,  {'userId': self.userId})
        else:
            query = """SELECT p.permission FROM users u
JOIN userRoles ur ON u.userId = ur.userId
JOIN assignedRoles ar ON ur.assignedRoleId = ar.assignedRoleId
JOIN assignedRolePermissions arp ON ar.assignedRoleId = arp.assignedRoleId
JOIN permissions p ON arp.permission = p.permission
WHERE u.userId = %(userId)s AND (arp.gameId is NULL OR arp.gameId = %(gameId)s)
UNION
SELECT p.permission FROM assignedRolePermissions arp
JOIN permissions p ON arp.permission = p.permission
WHERE arp.assignedRoleId IN (
    SELECT assignedRoleId
    FROM assignedRoles
    WHERE roleName IN ('public', 'user')
) AND (arp.gameId is NULL OR arp.gameId = %(gameId)s)
UNION
SELECT generatedRolePermissions.permission AS permission FROM `registrations`
JOIN generatedRoles ON generatedRoles.generatedRoleId = registrations.generatedRoleID
JOIN generatedRolePermissions ON generatedRolePermissions.generatedRoleID =  generatedRoles.generatedRoleId
JOIN teams ON registrations.teamId = teams.teamId
WHERE `userId` = %(userId)s AND ((teams.canPlaySince IS NOT NULL and generatedRolePermissions.eligible = 1)
OR (teams.canPlaySince IS NULL and generatedRolePermissions.eligible = 0)) AND (generatedRoles.gameId IS NULL OR generatedRoles.gameId = %(gameId)s)"""
            cursor.execute(query, {'userId': self.userId, 'gameId': gameId})
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        return result