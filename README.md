# Random survey web app
### Installation
`$ pip install -r Requirements.txt`

Configure your database connection [here](https://github.com/Stamper/rurvey/blob/master/rurvey/settings.py#L78). You can choice a RDBMS from the [list](https://docs.djangoproject.com/en/2.2/ref/databases/).
### Project bootstrap
```
$ python manage.py migrate
$ python manage.py createsuperuser
```

Regular django-based app flow
### Run server
`$ python manage.py runserver`

Web app URL's:
 - [random survey question](http://127.0.0.1:8000)  
 - [admin dashboard](http://127.0.0.1:8000/admin/)
 - [statistics](http://127.0.0.1:8000/admin/questions/statistics/)
### Tests
`$ python manage.py test`

