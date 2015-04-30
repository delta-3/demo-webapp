Created with Django 1.8
<br />
All Python code tested with Python 2.7.6
<br />
Project name: vulnerable
<br />
App name: delta3


##Setup

1. Modify settings.py to include the the app `secure_app` 
2. Modify settings.py to add middleware to include `secure_app.middlewares.Repair`
3. `ln -s ../django-auto-repair/secure_app/ ./`
4. `python manage.py syncdb`
5. Run `pip install -r requirements.txt`
6. Clone this repo to separate directory and start on port 8888
'python manage.py runserver 127.0.0.1:8888`
7. Start main server which defaults to port 8000
`python manage.py runserver`

##Testing

/admin use username delta3 password is admin

#####Sql injections for search page:
1. `" OR 1=1;--`
2. `" UNION ALL SELECT age, username, password FROM delta3_user;--`

#####XSS for comments page:
1. a variation of script tag, except for all lowercase (e.g., `<scRipt>...</scRipt>`)


##Running Demo

###Register(Parse exception)
Do no use numbers in first, last, 

1. Start off creating 3 'good' users with ages 20-30 in FF browser incognito mode
2. Go to database and show everyone it has the user data
3. Move to chrome incognito and act as bad guy with 2 digit number follow by letter 
4. This should crash !
5. Show database explain input was tagged as bad
6. Show filter with should allow only 2 digits (possibly)
7. Go back to malicious user, enter 2 characters for age
8. Crash, show request table, show filter, explain filter changed to be more generic
9. Go back to malicious enter 2 characters for age, show bad input was blocked


###Search (Sql injection)

1. Clear database
2. Execute the sql injection showing it works
6. `" UNION ALL SELECT age, username, password FROM delta3_user;--`
1. Now say "But with our system"
2. Clear database
1. With FF (good guy) search for at least 3 things
2. With Chrome (bad guy) enter `
 `" UNION ALL SELECT * FROM delta3_user;--`
3. Show request database, it is tagged as bad
4. Show filter that it generated
6. Now do `" UNION ALL SELECT age, username, password FROM delta3_user;--`
