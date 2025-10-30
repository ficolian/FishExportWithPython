#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn exportfish.wsgi