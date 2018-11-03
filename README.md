# Imaginashion - Product Recognition and Retrieval

## Introduction

This is a small example of a Computer Vision Application using jQuery File Upload in Django. 

Here, you'll find a Django project with a minimal app. You can run the example standalone by cloning the repository, running the migrations, adding the keys and starting the server.

You will require an API Key from Google Cloud Vision in order to setup your API calls in file 'label/label.py' as well as an Amazon API Key for running queries as set up in 'fileupload/fetch_py3'


## Overview

* Upload files
* Various UI Features for uploads including Drag and Drop
* Analyse Image using Google Cloud Vision
* Retrieve matching Amazon Products using the Amazon Product Search API


## Requirements

* Django
* Python Imaging Library
* Google Python Client API

If you do not get PIL to work (_pillow_ is a replacement package that works
with virtulalenvs), use FileField instead of ImageField in
fileupload/models.py as commented in the file.

Set up a Trial Account on Google Console which will provide $300 worth of free credits for testing purposes.

Set up Amazon Account to retrieve Keys for authentication with API calls.


## Installation

* Running on Python 3.5.4 and Django 1.9.8
* pip install -r requirements.txt (will install django and pillow)
* python manage.py migrate
* python manage.py runserver
* configure Amazon API Key
* configure Google Cloud Vision API Key
* go to localhost:8000/upload/new/ and upload some files


## References

[jQuery-File-Upload](http://aquantum-demo.appspot.com/file-upload) is developed by Sebastian Tschan, with the source available on [github](https://github.com/blueimp/jQuery-File-Upload). Example code is [ported to Django](https://github.com/sigurdga/django-jquery-file-upload) by Sigurd Gartmann ([sigurdga on github](https://github.com/sigurdga/)).


## License

MIT, as the original project. See LICENSE.txt.
