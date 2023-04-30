from flask import Flask, render_template, request
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Flask_Projects/Practice/instance/mydb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mydb = SQLAlchemy(app)

class Todo(FlaskForm):
    text = StringField("Todo", validators=[DataRequired()])
    submit = SubmitField("Add")

class User(mydb.Model):
    id = mydb.Column(mydb.Integer, primary_key=True)
    Text = mydb.Column(mydb.String(200))
    def __repr__(self):
        return f"Task {self.id}: {self.Text}"

@app.route('/', methods=["POST", "GET"])
def index():
    todo = Todo()
    if todo.validate_on_submit():
        new_todo = User(Text=todo.text.data)
        mydb.session.add(new_todo)
        try:
            mydb.session.commit()    
        except:
            mydb.session.rollback()
    todo_list = User.query.all()
    return render_template('index.html', template_form=todo, temp_list=todo_list)