# Academic Institute Management System

Buitl Using Python - Django

## Frontend

HTML - CSS - JAVASCRIPT

## Backend

Python - Django

## Database:

MySQL - (Easy to replace with any other SQL or Sqlite Database)

![AIMS Login Page](https://github.com/AhsanJoyia/Academic-Institute-Management-System/blob/master/media/AIMS%20Login%20Page.jpeg?raw=true)
![AIMS Reset Password Page](https://github.com/AhsanJoyia/Academic-Institute-Management-System/blob/master/media/AIMS%20Reset%20Password%20Page.jpeg?raw=true)
![AIMS Admin Page](https://github.com/AhsanJoyia/Academic-Institute-Management-System/blob/master/media/AIMS%20Admin%20Page.jpeg?raw=true)
![AIMS Staff Page](https://github.com/AhsanJoyia/Academic-Institute-Management-System/blob/master/media/AIMS%20Staff%20Page.jpeg?raw=true)
![AIMS Student Page](https://github.com/AhsanJoyia/Academic-Institute-Management-System/blob/master/media/AIMS%20Student%20Page.jpeg?raw=true)

## Installation Procedure:

### 1: Clone and fork this repostory

### 2: Download and install python and any server like xampp or wampp

### 3: Add python path to environment variable

### 4: Open project, go to terminal and run this command. pip install -r requirements.txt

### 5: Now rename .envsample file to .env and your email, email password, captcha secret key and captcha site key.

#### Note: To create captcha secret key and secret site key follow this link

https://www.google.com/recaptcha

### Make sure that the email you are going to add allow less secure app enable.

To do this follow this link
https://myaccount.google.com/security

### If you don't provide captcha secret and site key then captcha on this project would't work

### If you don't enable less secure app access then password reset option would'nt work

### 6: Open xampp sever, create database, database name should be aims. (If you want to change database name then navigate to aims/settings.py and find this code


` DATABASES = {

` 'default': { # 'ENGINE': 'django.db.backends.sqlite3', # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

` 'ENGINE':'django.db.backends.mysql',

` 'NAME':'aims'

` 'USER':'root'

` 'PASSWORD':''

` 'HOST':'localhost'

` 'PORT':'3306'

`    }
` }


### Change aims to whatever you want)

### 7: Now open your terminal and type these commands one by one

python manage.py makemigrations
python manage.py migrate

### 8: Now open your terminal and type python manage.py createsuperuser

It will ask for username, type your username.
Then it will ask for email, type your email.
Then it will ask for password, type your password

### 9: Now open your terminal and type python manage.py runserver, you will see login page, just type the username and password you have created a minute ago

## Author

Malik Ahsan Joyia

### Note: This Project is Completed. I have no plan to add new features. It were a university project, so if you want to download documentation, Presentation, head over to the links below

#### Documentation

#### Presentation
