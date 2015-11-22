## hotshot-api
API hotshot-api displays the current and archival data products offer "hot shot" from website x-kom.pl 

### Endpoints
```
/hotshots - display all data
/hotshots/date/<date_hotshot> - display data from one day
```

### Install
```
pip install -r requirements.txt
```

### Run API
```
python manage.py runserver
```
***
### Examples:
* http://hs-api.tk/hotshots
* http://hs-api.tk/hotshots/date/2015-11-20
