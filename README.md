# Django Rest, this example is with court tennis reservations

<!-- For more detail, please visit:
> [Django & MongoDB CRUD example with Rest Framework](https://bezkoder.com/django-mongodb-crud-rest-framework/) -->



## Create virtual environment

Python3 and pip3 must be installed, this example was made with Python 3.8.10 and pip 21.2.4.   

upgrade pip with:
```python3
python3 -m pip install --upgrade pip
```
Install Virtualenv to create the virtual environment, with:
```python3
pip3 install virtualenv
```
go to the project with your console, there create the virtual environment, with:  
```bash
virtualenv venv
```
enter the virtual environment, with:
```bash
source venv/bin/activate
```
if you want to exit the virtual environment, type in console:
```bash
deactivate
```
Inside the environment you can install the packages, run the file requirements.txt, with:
```python3
pip3 install -r requirements.txt
```

## Running the Application   
   
Create the DB tables first:
```
python3 manage.py makemigrations 
python3 manage.py migrate
```
Run the development web server:
```
python manage.py runserver 8080
```
Open the URL http://localhost:8080/ to access the application.