#!/bin/bash
#docker build -t web:latest .
#docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest

docker build -t registry.heroku.com/dry-lake-88654/web .
docker push registry.heroku.com/dry-lake-88654/web
heroku container:release -a dry-lake-88654 web

# heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a dry-lake-88654
# heroku config:set DEBUG=0 -a dry-lake-88654
heroku open -a dry-lake-88654
# heroku addons:create heroku-postgresql:hobby-dev -a dry-lake-88654

heroku run python manage.py migrate -a dry-lake-88654
# heroku run python manage.py createsuperuser -a dry-lake-88654
# heroku run python manage.py collectstatic -a dry-lake-88654
# heroku ps:restart web -a dry-lake-88654
# heroku logs -a dry-lake-88654