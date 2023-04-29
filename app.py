from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_profiler import Profiler

app = Flask(__name__)
""" profiler=Profiler(app) """

app.config['SECRET_KEY'] = '12345678'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Flask_Projects/Experiment/instance/mydb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mydb = SQLAlchemy(app)

class User(mydb.Model):
    id = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(50), index=True, unique=True)
    surname = mydb.Column(mydb.String(80), index=True, unique=True)
    def __repr__(self):
        return f"<{self.name} {self.surname}>"

class Login(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/', methods=['POST', 'GET'])
def Index():
    login_form = Login()
    if login_form.validate_on_submit():
        new_user = User(name=login_form.name.data, surname=login_form.surname.data)
        mydb.session.add(new_user)
        try:
            mydb.session.commit()
        except:
            mydb.session.rollback()
    return render_template("index.html", template_form=login_form)

if __name__ == '__main__':
    app.run(debug=False)