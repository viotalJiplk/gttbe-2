# Gttournament backend 2
Second version of backend for gttournament.

(first version: https://github.com/Vitond/gttournament-backend)

## Install
1. install python3
2. `pip install -r requirements.txt`
3. rename config-template.py to config.py
4. install Mysql like database
5. create db account
6. add credentials to config.py
7. setup database with db initdb.sql
8. grant db account access to database
9. create new app on https://discord.com/developers/applications
10. go to OAuth2 and fill config.py with info from here

## Running application
1. set enviroment variable `FLASK_APP=app.py`
2. run `flask run`
3. you can find all premade tests over at: http://127.0.0.1:5000/test/testpages/index.html

## Production
**Not yet ready!**
set enviroment variable `PROD` to anything
