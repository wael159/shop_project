import flask_wtf
import wtforms
from wtforms import validators as vld

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign up")

class searchquery(flask_wtf.FlaskForm):

    searchby = wtforms.SelectField("search method:", choices=[('name', 'name'), ('category', 'category'),('id', 'id')],validators=[vld.DataRequired()])
    value = wtforms.StringField("value:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Search")


class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Name:", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password:", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign in")


