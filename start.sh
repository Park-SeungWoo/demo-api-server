#!/bin/bash

# make migrations
#python proj_name/manage.py makemigrations main_app_name

# migrate db
python manage.py migrate

# run server
python manage.py runserver 0.0.0.0:8000 --noreload