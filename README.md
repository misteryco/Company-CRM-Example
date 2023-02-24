Python Web Framework with Django and Django REST framework

The main idea behind the project is to create an simple operational REST application for companies which allows:

● CRUD operations to manage companies

  Company instance have company name, logo and description.
  
● CRUD operations to manage company employees

  Employee have first name, last name, date of birth, photo, position, salary and company.

The project consists of main app called 'crm_for_companies'.

The project app uses SQLITE3 as a DBMS.

The app need a working CLOUDINARY account for photo and logo upload and serve.

The app uses environment variables to hide sensitive information.

The app have browsable API.

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

python manage.py startserver

python manage.py makemigrations

python manage.py migrate 

python manage.py runserver



URLs:

Companies:

· GET 'localhost:8000/api_companies/' – lists all companies with employees data.

· GET 'localhost:8000/api_companies/?company_id={COMPANY_ID}' – specific  companie by company ID with employees.

· GET 'localhost:8000/api_companies/details/{COMPANY_ID}' –  lists one company.

· PUT 'localhost:8000/api_companies/details/{COMPANY_ID}' –  update one company.

· DELETE 'localhost:8000/api_companies/details/{COMPANY_ID}' –  delete one company.


Employess:

· GET 'localhost:8000/api_employees/' – lists all employees with companies data.

· GET 'localhost:8000/api_ employees/?company_id={COMPANY_ID}' – lists all employees within specific company.

· GET 'localhost:8000/api_ employees/details/{EMPLOYEE_ID}' – lists one employee.

· PUT 'localhost:8000/api_ employees/update/{EMPLOYEE_ID}' – update one employee.

· DELETE 'localhost:8000/api_ employees/delete/{EMPLOYEE_ID}' – delete one employee.





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
