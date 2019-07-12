# Random survey web app
### Installation
`$ pip install -r Requirements.txt`
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

