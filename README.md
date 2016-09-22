## Comment Micro-services
[![Build Status]()]() <br />
Simple Example for REST Services With Django Rest Framework
>Create the Python Virtual environment and clone the project and follow the below steps.
<b> Installing </b>
```sh
$ pip install -r requirements.txt
$ pip install psycopg2
```
<b> Configuration </b>
> Configure the db with postgres in settings. Create the tables as shown in the models. Run the migrations as shown below. <b>Syncdb</b> is deprecated from the version 1.9.

<b> Database </b>
> Use the <b>rest.sql</b> for creating database and tables.

<b> Run Migration</b>
```sh
$ python manage.py makemigration
```
<b> Run Migrate</b>
```sh
$ python manage.py migrate
```
<b> Run Server</b>
```sh
$ python manage.py runserver
```
> By running following Url it will throws the error. It is related to foreign key. 
> So first post the data as show in the POST data Section.
> 
<b> Rest URL/ GET URL </b>
```sh
 http://127.0.0.1:8000/master/users/
```

<b> POST Data </b>
``` sh 
$ curl -X POST http://127.0.0.1:8000/master/users/ -d '{"id":"1","repayment_type_name":"MANUAL", "fk_status":"1","last_modified_date":"2016-01-12 00:00:00+05:30","last_modified_by":"1"}' -H "Content-Type: application/json"
```
<b> GET URL for single resource </b>
```sh
 http://127.0.0.1:8000/master/users/1/
```
<b> Delete resource </b>
```sh
curl -X DELETE http://127.0.0.1:8000/master/users/1/
```

## Run Virtualenv
```sh
env\Scripts\activate.bat
```

## Migration

- python manage.py makemigrations commentengine --name of app
- python manage.py migrate commentengine --name of app

