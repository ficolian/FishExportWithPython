-- make migration
python manage.py makemigrations

-- submit migaration
python manage.py migrations

-- create user
python manage.py createsuperuser

-- create module
python manage.py startapp pages

--runserver
python manage.py runserver

--setup git
git init 

git remote add origin https://github.com/ficolian/FishExportWithPython.git

git push -f origin main

