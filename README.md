Created with Django 1.8
<br />
All Python code tested with Python 2.7.6
<br />
Project name: vulnerable
<br />
App name: delta3


##Setup

1. Modify settings.py to include the the app `secure_app` 
2. Modify settings.py to add middleware to include ``secure_app.middlewares.Repair`
3. ln -s ../django-auto-repair/secure_app/ ./
4. python manage.py syncdb
5. Run `pip install -r requirements.txt`



##Testing
#####Sql injections for search page:
1. `" OR 1=1;--`
2. `" UNION SELECT * from delta_user;--`

#####XSS for comments page:
1. a variation of script tag, except for all lowercase (e.g., `<scRipt>...</scRipt>`)
