Python Web Framework with Django and Django REST framework

The main idea behind the project is to create a simple operational REST application for companies which allows:

● CRUD operations to manage companies

Company instance have 'company name', 'logo', 'owner' and description.

● CRUD operations to manage company employees

Employee have 'first name', 'last name', 'date of birth', 'photo', 'position', 'salary' and 'company'.

● CRUD operations to create and authenticate users.

Users have 'first name', 'last name', 'email', 'password'.

The project consists of main app called 'crm_for_companies'.

The project app uses POSTGRESS as a DBMS.

The app need a working CLOUDINARY account for photo and logo upload and serve.

The app uses environment variables to hide sensitive information.

The app have browsable API.

HOW TO BUILD:

- In a new vnv:

- pip install requirements.txt

- setup your .env file according .env.example replacing necessary fields.

HOW TO USE:

- In "crm_for_companies" folder run:

python manage.py runserver

python manage.py makemigrations

python manage.py createsuperuser

python manage.py migrate

===== START NEW COMMAND FOR CELERY ====

IN NEW TERMINAL In "crm_for_companies" folder run:

celery -A crm_for_companies worker -l info -E

===== end NEW COMMAND FOR CELERY ====

python manage.py runserver

- You have to logg in :

'localhost:8000/admin/' - login to use the app

'localhost:8000/swagger/' - open this swagger so you can learn available endpoint and test them

DISCLAIMER: This app is not a fully operational product, it's not intended for commercial use and has many features that
haven't been properly tested or developed.
