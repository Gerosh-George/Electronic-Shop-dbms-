# Electronic-Shop-dbms
Django project to implement the basic working of an Electronic Shop.
MySQL database is used for backend purpose.

### Setup to run the project:
- pip install django
- pip install django-crispy-forms
- pip install django-phone-field

### Some commands to start django project:
(Note: These are for creating a new project for yourself)
- To initialize the project: django-admin startproject project_name 
- To create an app in the project: python manage.py startapp app_name


To run the server - python manage.py runserver

Note: In the settings.py file of the mysite folder, the database settings dictionary needs to be updated with your database credentials to successfully connect. 

If you are using MYSQL then do the following setup:
- pip install mysqlclient
- python manage.py migrate
