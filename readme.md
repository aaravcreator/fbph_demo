
# Django Based Phishing Site Demo(ONLY FOR EDU PURPOSES)
## Description

This project demonstrates phising attack ( the login ui is of facebook ) and it uses django in the backend to collect credentials




## Table of Contents (Optional)

- [Installation](#installation)


## Installation (REQUIRED )
Go to repo folder 
```bash
cd fbph_demo
```
Firstly create new Python virtual environment using
```bash
python -m venv myenv
```
# Activate that environment
For windows
```bash 
myenv\Scripts\activate
```
For Linux
```bash
myenv/bin/activate
```
After the successful activation you can see (myenv) infornt of every terminal cmd change directory to project directory(directory where manage.py file resides)

## Dependency Install
We need to install django and other dependencies\
here we have requirements.txt file with is list of all required dependencies\
Run  
```bash
pip install -r requirements.txt
```
change directory to project directory to run migrations and server
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```
and then finally
```bash
python manage.py runserver
```

## SCREENSHOTS
![Login Page](./screenshots/login.png)
![Success Page](./screenshots/success.png)
![Django Admin Credentials Page](./screenshots/credentials.png)
