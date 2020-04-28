
# This is a crowd funding web application  

     Still under development...  

<br>

## Prerequisites 
* Python (>= 3.4 required) 
* MySQL (or) PostgreSQL
<br>

## Installation 
**To run the application after downloading you need to do a few steps:**  
  
* ```pip install virtualenv```  
* ```cd crowd-funding```  
* ```virtualenv env```  
* ```source env/bin/activate```  
* ```pip install -r requirements.txt```  
* ```cp config.example.ini config.ini```  
  
* Start replacing the environment variables in the config.ini  file with yours.  
  **PS:** You can generate secret key to the project from [here](https://djecrety.ir/).  
  
* ```python manage.py migrate```
* ```python manage.py seed projects --number=20 2> /dev/null``` # if you wanted to seed data to your database #
* ```python manage.py runserver```  
  
#### And by now you should have the application running.

<br>

## External Resources
* [To create the custom user model](https://testdriven.io/blog/django-custom-user-model/)


