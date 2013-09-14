Django Bootstrap Starter Project
================================
This project makes it really easy to create a Django project and publish it to Heroku.

See Demo:  http://django-bootstrap2.herokuapp.com


What is included?
-----------------
* Django 1.5
* Heroku settings
* Python Social Auth. Oauth for Facebook, Google, Yahoo!
* Jquery
* Bootstrap


What you need to get started?
-----------------------------

### Mininmum requirements

* Heroku account


### Advance requirements

* Facebook Oauth keys: FACEBOOK_APP_ID, FACEBOOK_API_SECRET
* Google OAuth keys: SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET



Setup Steps
===========

* git clone git@github.com:ddehghan/django-bootstrap-starter-project2.git myproject
* cd myproject
* heroku create <my_cool_project_name>
* source myproject/settings_local.env.sh
* sh myproject/settings_local.heroku.sh
* git push heroku master
* heroku run python manage.py syncdb

* Great Success! You are done.


Helpful Commands
================


* Check settings

> heroku config
> printenv


### View logs and status
> heroku logs
> heroku ps
> heroku config


### Database

Deployment of Django on Heroku https://devcenter.heroku.com/articles/django

> heroku run python manage.py syncdb

> heroku run python manage.py migrate website


> heroku domains:add www.example.com


> python manage.py collectstatic --noinput;
> heroku config:add DISABLE_COLLECTSTATIC=1         # To disable static collection

To drop heroku database:
> heroku pg:reset DATABASE


How to get GoogleOauth key
==========================

* Got to https://code.google.com/apis/console
* Go to API Access tab
* Create new Client ID for web applications
* add this urls http://localhost:8000/complete/google-oauth2/
* copy Client ID: and Client secret to SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
