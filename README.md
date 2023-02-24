Python Web Framework with Django and Django REST framework

The main idea behind the project is to create an simple operational REST application for companies which allows:

● CRUD operations to manage companies

  Company instance have company name, logo and description.
  
● CRUD operations to manage company employees

  Employee have first name, last name, date of birth, photo, position, salary and company.

The project consists of main app called 'crm_for_companies'.

The project app uses SQLITE3 as a DBMS.

The app need a working CLOUDINARY account for photo and logo upload and serve.

The project app uses environment variables to hide sensitive information.

HOW TO BUILD:

- In a new vnv:

- pip install requirements.txt

- setup your .env file:

DEBUG=on

SECRET_KEY='YOUR_SECRET'

CLOUDINARY_CLOUD_NAME='YOUR_CLOUDINARY_CLOUD_NAME'

CLOUDINARY_API_KEY='YOUR_CLOUDINARY_API_KEY'

CLOUDINARY_API_SECRET='YOUR_CLOUDINARY_API_SECRET'


HOW TO USE:

- In "crm_for_companies" folder run:

python manage.py makemigrations

python manage.py migrate 

python manage.py startserver

- JSON format data for input:
Company JSON Format
{
    "name": String,
    "description": String,
    "logo": "logo_filelocation from PC for eaxample : D:/03.jpg"
}

Employee JSON Format:

{
    "first_name": String,
    "last_name": String,
    "date_of_birth": Data, for example: "2006-07-04",
    "photo": "lphoto_filelocation from PC for eaxample : D:/03.jpg",
    "position": String,
    "salary": Integer,
    "company": Integer
}


DISCLAIMER: This app is not a fully operational product, it's not intended for commercial use and has many features that haven't been properly tested or developed.
