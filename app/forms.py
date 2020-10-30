import flask_wtf
import wtforms
from wtforms import validators as vld

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign up")

class searchquery(flask_wtf.FlaskForm):

    searchby = wtforms.SelectField("search method:", choices=[('name', 'name'), ('category', 'category'),('id', 'id'),('author_name', 'author_name'),('year','year')],validators=[vld.DataRequired()])
    value = wtforms.StringField("value:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Search")


class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign in")


class Add_books(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    price = wtforms.StringField("Price:", validators=[vld.DataRequired()])
    stock_quantity   = wtforms.StringField("stock quantity")
    category=wtforms.StringField("Category:", validators=[vld.DataRequired()])
    description = wtforms.StringField("description:", validators=[vld.DataRequired()])
    author_name = wtforms.StringField("author_name:", validators=[vld.DataRequired()])
    year = wtforms.StringField("year:", validators=[vld.DataRequired()])
    submit=wtforms.SubmitField("Submit")