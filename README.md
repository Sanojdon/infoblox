# infoblox
Sample Project Assessment for Infoblox
The project has been made with Django 3.1.1
Django Rest Framework : 3.11.1
This is a project created with basic Django and Django Rest Framework.
Please setup your Postgresql Database, with the user and database given below, for error free running
Database : info
User : sample_user
Password : infoblox123

Steps to run the project
1. pipenv shell #All the necessary packages are put up in the Piplock file
2. get into the project folder
3. run python3 manage.py runserver
4. The server starts running and may ask you for migrations
5. run python3 manage.py migrate
6. Create a super user to have the admin privileges
7. /jsonread/api : Will list all the data in the database
8. /jsonread/api/all : Will let you enter the details for the database

Command Line executables:
python3 manage.py add_data <location of your json file> : Will run the json file and enter into the database
python3 manage.py read_data <id of the user> : Will print the firstname and last name of the appropriate user
