# Profiles REST API

REST API providing basic functionality for managing user profiles.

## Setup

git clone <HTTPS url> --> download the content at (OS:)/Users/User/

## Connect app to localhost

cd to that directory to setup VM env
```bash
vagrant up
```

Connect to the VM env
```bash
vagrant ssh
```

To runserver on localhost
```bash
workon profiles_api
cd /vagrant/src/profiles_project
python manage.py runserver 0:8080
```
