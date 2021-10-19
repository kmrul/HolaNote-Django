# HolaNote
A user based note who can note public and privately.

# Features
- User can signup and login
- Get email account vaification
- Sow public everyone note
- show only his/her private note
- Own note can add, edit, update, and delete
- Set his note on public or private


# Create Database and Database Users
- sudo su - postgres
- psql
- CREATE DATABASE database_holanote;
- CREATE USER holanote_role WITH PASSWORD 'holanote_password';
- GRANT ALL PRIVILEGES ON DATABASE database_holanote TO holanote_role;
- \q
- exit


## Technologes: 
- Djanog, 
- Postgresql, SQLite 
- Docker

## some of command
sudo docker-compose run web django-admin startproject mysite .

sudo chown -R $USER:$USER .

# create new app
docker exec [container_name] python manage.py startapp [app_name]

docker-compose run web python holdanote/manage.py migrate

# Create superuser
docker-compose run web python holanote/manage.py createsuperuser
