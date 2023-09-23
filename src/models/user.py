from utils.db import getConnection, dbConn
import datetime
import requests
from config import discord
from requests import post
from datetime import date, datetime, timedelta
import json

class UserModel:

    def __init__(self, userid = '', refresh_token = '', access_token = '', expires_in = '', name='', surname='', adult='', school_id=''):
        if(not isinstance(expires_in, datetime)):
            expires_in = datetime.utcfromtimestamp(expires_in)
        self.userId = userid
        self.surname = surname
        self.name = name
        self.adult = adult
        self.schoolId = school_id
        self.__access_token = access_token
        self.__refresh_token = refresh_token
        self.__expires_in = expires_in

    def __str__(self):
        return json.dumps({
            "userId": self.userId,
            "surname": self.surname,
            "name": self.name,
            "adult": self.adult,
            "schoolId": self.schoolId,
            "discord_user_object": self.getDiscordUserObject()
        })

    @classmethod
    @dbConn(autocommit=True, buffered=True)
    def updateOrCreateUser(cls, cursor, db, userid = '', refresh_token = '', access_token = '', expires_in = '', name='', surname='', adult='', school_id=''):
        if(refresh_token == '' or access_token == '' or userid == '' or userid == ''):
                raise Exception("Missing something in request.")
       
        values = {
            'userid': userid,
            'refresh_token': refresh_token,
            'access_token': access_token,
            'expires_in': expires_in,
        }

        # try if user already exists
        query = "UPDATE users SET `refresh_token` = %(refresh_token)s, `access_token` = %(access_token)s, `expires_in` = %(expires_in)s"

        if(name != ''):
            values["name"] = name
            query += ", `name` = %(name)s"
        if(surname != ''):
            values["surname"] = surname
            query += ", `surname` = %(surname)s"
        if(adult != ''):
            values["adult"] = adult
            query += ", `adult` = %(adult)s"
        if(school_id != ''):
            values["school_id"] = school_id
            query += ", `schoolId` = %(school_id)s"

        query += " WHERE `userid` = %(userid)s;"

        cursor.execute(query, values)
        if(cursor.rowcount != 1):
            # user does not exist yet
            if(name == '' or surname == '' or adult == '' or school_id == ''):
                raise Exception("Missing something in request.")
            values = {
                'userid': userid,
                'refresh_token': refresh_token,
                'access_token': access_token,
                'expires_in': expires_in,
                'name': name,
                'surname': surname,
                'adult': adult,
                'schoolId': school_id,
            }
            query = "INSERT INTO users (`userid`, `access_token`, `refresh_token`, `expires_in`, `surname`, `name`, `adult`, `schoolId`) VALUES (%(userid)s, %(access_token)s, %(refresh_token)s, %(expires_in)s, %(surname)s, %(name)s, %(adult)s, %(schoolId)s);"
            cursor.execute(query, values)
            
        return UserModel(userid=userid, refresh_token=refresh_token, access_token=access_token, expires_in=expires_in, name=name, surname=surname, adult=adult, school_id=school_id)

    @classmethod
    def getByCode(cls, code, redirect_uri, name, surname, adult, school_id):
        '''exchange code for access and refresh tokens'''
        data = {
            'client_id': discord["client_id"],
            'client_secret': discord["client_secret"],
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
        tokenReq = UserModel.tokenEndpoint(data)
        
        ''' now lets get discords user object'''
        user = UserModel(access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"])
        userObject = user.getDiscordUserObject()

        return UserModel.updateOrCreateUser(userid = userObject["id"], refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"], name=name, surname=surname, adult=adult, school_id=school_id)

    @classmethod
    @dbConn(autocommit=True, buffered=True)
    def getById(cls, userId, cursor, db):
        sql = "SELECT userId, surname, name, adult, schoolId, access_token, refresh_token, expires_in  FROM users WHERE userId=%(userId)s"
        cursor.execute(sql, {'userId': userId})
        row = cursor.fetchone()
        if row is None:
            return None
        return UserModel(userid=row[0], surname= row[1], name = row[2], adult = row[3], school_id = row[4], access_token=row[5], refresh_token=row[6], expires_in=row[7])
    
    def getDiscordUserObject(self):
        today = datetime.today()
        if(self.__expires_in < today):
            self.__refresh_token_refresh()
        try:
            headers = {
                "Authorization": "Bearer " + self.__access_token
            }
            userObjectReq = requests.get('%s/oauth2/@me' % discord['api_endpoint'], headers=headers)
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
            tokenReq = post('%s/oauth2/token' % discord['api_endpoint'], data=data, headers=headers)
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
            'client_id': discord["client_id"],
            'client_secret': discord["client_secret"],
            'grant_type': 'authorization_code',
            'grant_type': 'refresh_token',
            'refresh_token': self.__refresh_token
        }
        tokenReq = UserModel.tokenEndpoint(data)

        UserModel.updateOrCreateUser(userid = self.userId, refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"])

        self.__refresh_token = tokenReq["refresh_token"]
        self.__access_token = tokenReq["access_token"]
        self.__expires_in = tokenReq["expires_in"]

        return self
    
    @dbConn(autocommit=True, buffered=True)
    def delete(self, cursor, db):

        # try if user already exists
        query = "DELETE FROM users WHERE `userId` = %(userId)s"
        cursor.execute(query, {"userId": self.userId})

        self.userId = ""
        self.surname = ""
        self.name = ""
        self.adult = ""
        self.schoolId = ""
        self.__access_token = ""
        self.__refresh_token = ""
        self.__expires_in = ""