## hotshot-api
API hotshot-api displays the current and archival data products offer "hot shot" from website x-kom.pl 

### Endpoints
```
/hotshots - display all data
/hotshots/date/<date_hotshot> - display data from one day
```

### Install packages
```
pip install -r requirements.txt
```

### Run API
```
python manage.py runserver
```
***
### Examples:
* http://hotshot.ga/hotshots
* http://hotshot.ga/hotshots/date/2015-11-20
