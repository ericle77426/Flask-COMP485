# A simple code for server monitoring system using Flask

### Overview
+ This system checks all servers it was configured to monitor every 5 seconds and display "Online" or "Offline" status accordingly. 

### Functions
This monitoring system has following functions:
+ View all monitored servers and display their status
+ Login / Logout
+ (*) Add new server to monitor
+ (*) Remove existing server
+ (*) Add new admin user
+ (*) Remove existing admin user


> *: those functions only available when user is logged in

### Usage:
For the flask you need to install python in https://www.python.org/,
After install open cmd you can cd to the python folder then srite command "pip install virtualenv" to check the pip version
Use the command cd in cmd move to the folder that you keep the Flask-COMP485 in github then write a command "virtualenv venv" for install setuptools python in that folder
In this test we use sqlite 3. you can free download at https://www.sqlite.org/index.html
First time see this web app? please run the following commands to init database:
```
$ from server import init_db
$ init_db()
```
Now you are ready to go: <br/>
```
$ python server.py
```
And enjoy, access: http://127.0.0.1:5000

