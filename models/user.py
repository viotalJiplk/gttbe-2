from utils.db import getConnection
import datetime
import requests
from config import discord
from requests import post

class UserModel:
    def __init__(self, userid = '', refresh_token = '', access_token = '', expires_in = '', name='', surname='', adult='', school_id='', dbsync=True):
        if(dbsync):
            if(refresh_token == '' or access_token == '' or userid == ''):
                    raise Exception("Missing something in request.")
            values = {
                'userid': userid,
                'refresh_token': refresh_token,
                'access_token': access_token,
                'expires_in': datetime.datetime.now() + datetime.timedelta(0,expires_in),
            }

            db = getConnection(autocommit=True)
            cursor = db.cursor(buffered=True)

            # try if user already exists
            query = "UPDATE users SET `refresh_token` = %(refresh_token)s, `access_token` = %(access_token)s, `expires_in` = %(expires_in)s WHERE `userid` = %(userid)s;"
            cursor.execute(query, values)
            if(cursor.rowcount != 1):
                # user does not exist yet
                if(name == '' or surname == '' or adult == '' or school_id == ''):
                    raise Exception("Missing something in request.")
                values = {
                    'userid': userid,
                    'refresh_token': refresh_token,
                    'access_token': access_token,
                    'expires_in': datetime.datetime.now() + datetime.timedelta(0,expires_in),
                    'name': name,
                    'surname': surname,
                    'adult': adult,
                    'schoolId': school_id,
                }
                query = "INSERT INTO users (`userid`, `access_token`, `refresh_token`, `expires_in`, `surname`, `name`, `adult`, `schoolId`) VALUES (%(userid)s, %(access_token)s, %(refresh_token)s, %(expires_in)s, %(surname)s, %(name)s, %(adult)s, %(schoolId)s);"
                cursor.execute(query, values)
            cursor.close()
            db.close()
        self.userId = userid
        self.surname = surname
        self.name = name
        self.adult = adult
        self.schoolId = school_id
        self.__access_token = access_token
        self.__refresh_token = refresh_token
        self.__expires_in = expires_in

    @staticmethod
    def getByCode(code, redirect_uri, name, surname, adult, school_id):
        '''exchange code for access and refresh tokens'''
        data = {
            'client_id': discord["client_id"],
            'client_secret': discord["client_secret"],
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri
        }
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

        if(tokenReq["token_type"] != "Bearer"):
            raise Exception("discord token endpoint response  unknown token type")
        if(tokenReq["access_token"] == ""):
            raise Exception("discord token endpoint response  missing access_token")
        if(tokenReq["refresh_token"] == ""):
            raise Exception("discord token endpoint response  missing refresh_token")
        
        ''' now lets get discords user object'''
        user = UserModel(access_token = tokenReq["access_token"], dbsync = False)
        userObject = user.getDiscordUserObject()

        return UserModel(userid = userObject["user"]["id"], refresh_token = tokenReq["refresh_token"], access_token = tokenReq["access_token"], expires_in = tokenReq["expires_in"], name=name, surname=surname, adult=adult, school_id=school_id)

    @staticmethod
    def getById(userId):
        self.userId = userId
        sql = "SELECT userId, surname, name, adult, schoolId FROM users WHERE userId=%(userId)s"
        db = getConnection(autocommit=True)
        cursor = db.cursor(buffered=True)
        cursor.execute(sql, {"userid": userId})
        row = cursor.fetchone()
        cursor.close()
        db.close()
        return UserModel(userId=row[1], surname = row[2], name = row[3], adult = row[4], schoolId = row[5], dbsync=False)
    
    def getDiscordUserObject(self):
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
        return userObjectReq.json()