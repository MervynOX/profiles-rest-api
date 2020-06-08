# Profiles REST API

REST API providing basic functionality for managing user profiles.
***Below is the step by step to setup Django REST framework on your localhost***

## Setup

git clone <HTTPS url> --> download the content at (OS:)/Users/User/

## Connect app to development server

cd to that directory to setup VM env
```bash
vagrant up
```

Connect to the VM env
```bash
vagrant ssh
```

## On the VM environment for the **FIRST** time
#### Create a Python Virtual environment

```bash
mkvirtualenv profiles-api --python==python3
```

#### Install required Python packages

```bash
workon profiles-api
pip install django==1.11
pip install djangorestframework=3.6.2
```

## Create Migration and Sync Database
#### Connect app to development server, then
```bash
workon profiles-api
cd /vagrant/src/profiles_project
python manage.py makemigrations
python manage.py migrate
```

## To runserver on localhost
#### Connect app to development server, then
```bash
workon profiles-api
cd /vagrant/src/profiles_project
python manage.py runserver 0:8080
```
Then open a web browser and enter "127.0.0.1:8080" to enjoy :)
