# passerelle-python
Another REST API for La Passerelle des Corton

# Introduction

A REST API to manage bookings for La Passerelle.

* Backend : Python 3.5 / Django 1.9

* Embedded SQLite3 database

# Running The Application

To run the application run the following commands in passerelle-python.

* To setup the h2 database run.

		python3 server/manage.py makemigrations passerelle
		python3 server/manage.py migrate

* To run the server run.

        python3 server/manage.py runserver

# Test the API

When the server is running, the API is available here : http://0.0.0.0:8000.
Use the following urls when testing the API.

      GET     /rooms (passerelle.models Room)
      GET     /rooms/{id} (passerelle.models Room)
      
      GET     /bookings (passerelle.models Booking)
      GET     /bookings/{id} (passerelle.models Booking)
      
      GET     /closures (passerelle.models Closure)
      GET     /closures/{id} (passerelle.models Closure)
