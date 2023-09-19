# Gttournament backend 2
Second version of backend for gttournament.

(first version: [Vitond/gttournament-backend](https://github.com/Vitond/gttournament-backend))

## Docker install
1. download `.env`, `docker-compose.yml` and `create.sql`
```bash
wget https://raw.githubusercontent.com/viotalJiplk/gttbe-2/main/.env-template -O .env && wget https://raw.githubusercontent.com/viotalJiplk/gttbe-2/main/docker-compose.yml && wget https://raw.githubusercontent.com/viotalJiplk/gttbe-2/main/create.sql
```
2. get `client_id`, `client_secret` and add `redirect_url`
 - create Discord "App" [discord.com/developers/applications](https://discord.com/developers/applications?new_application=true)
 - go to *OAuth2* tab
 - copy `Client ID` and `Client Secret` and add them to `.env` file
 - add `http://127.0.0.1:5000/test/testpages/discord/login.html#getjws` to Redirects
3. create database
 - run 
 ```bash
 docker compose up -d
 ```
 - go to [127.0.0.1:5001](http://127.0.0.1:5001)
 - log in (Server: gtt-mariadb credentials are in `.env` file)
 - click SQL command
 - copy content from `create.sql` and click execute
4. done
 - run 
 ```bash
 docker compose up -d
 ```
 - you can find all premade "tests" over at: [127.0.0.1:5000/test/testpages/index.html](http://127.0.0.1:5000/test/testpages/index.html)

## Developer Install
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
11. add http://127.0.0.1:5000/test/testpages/discord/login.html#getjws to Redirects

## Running application
1. set enviroment variable `FLASK_APP=app.py`
2. run `flask run`
3. you can find all premade "tests" over at: http://127.0.0.1:5000/test/testpages/index.html

## Production
**Not yet ready!**
set enviroment variable `PROD` to anything
