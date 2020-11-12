sudo docker-compose run web django-admin startproject mysite .

sudo chown -R $USER:$USER .

# create new app
docker exec [container_name] python manage.py startapp [app_name]

docker-compose run web python holdanote/manage.py migrate

# Create superuser
docker-compose run web python holanote/manage.py createsuperuser