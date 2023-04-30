# First_project
Doing some stuff in order to understand the back-end.

#1 step
Create a virtual environment in cmd by typing the command "py -3 -m venv env". Instead of writing "env" you can choose any name, it's up to you.

#2 step
Activate your virtual environment by typing the command env\Scripts\activate

#3 step
Type those commands below in order to work with modules

*pip install flask-sqlalchemy*

*pip install WTForms*

*pip install Flask-CLI* This one you need to activate your flask shell

#4 step

Type into your terminal this command *SET FLASK_APP=app.py*
then type "flask shell"
After wards a flask shell will pop out, and you need to write these commands

">>> from app import app, mydb"

">>> mydb.create_all()"

">>> exit()"

#5 step 

Try to run your application by writing the command *flask run* in your terminal
