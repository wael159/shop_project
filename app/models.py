
from app import db
import flask_login
import werkzeug
from sqlalchemy.ext.hybrid import hybrid_property
from app.utils import ModelMixin
import datetime

from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask import redirect,request,url_for


Orders = db.Table('orders', db.Model.metadata,
                db.Column('id', db.Integer,primary_key=True),
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                  db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                  db.Column('quantity', db.Integer,default=1, nullable=False),
                  db.Column('created_at',db.DateTime, default=datetime.datetime.now),
                db.Column('updated_at',db.DateTime, onupdate=datetime.datetime.now))




class books(db.Model,ModelMixin): # SQL Table
    # Create attributes (SQL columns)
     # By default autoincremented
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price  = db.Column(db.Integer())
    stock_quantity = db.Column(db.Integer())
    category=db.Column(db.String(64))
    description=db.Column(db.String(64))
    author_name=db.Column(db.String(64))
    publish_year = db.Column(db.String(64))
    picture_path=db.Column(db.String(64))
    new_users = db.relationship('User', secondary=Orders, backref="books")




class User(db.Model, ModelMixin, flask_login.UserMixin): # SQL Table

    # Create attributes (SQL columns)
    id = db.Column(db.Integer(), primary_key=True)  # By default autoincremented
    name             = db.Column(db.String(64), nullable=False)
    email=db.Column(db.String(64)) # ADDED TO DB
    _password_hash    = db.Column(db.String(256))
    is_admin=db.Column(db.BOOLEAN(),default=False)

    #new_book=db.relationship('books',backref="new_users")
    new_books = db.relationship('books', secondary=Orders, backref="User")


    @classmethod
    def login_user(cls, name, pwd):
        user = cls.query.filter_by(name=name).first()
        print(user)
        if user and user.check_password(pwd):
            flask_login.login_user(user)
            return user
        return False

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, pwd):
        self._password_hash = werkzeug.security.generate_password_hash(pwd)

    def check_password(self, pwd):
        return werkzeug.security.check_password_hash(self._password_hash, pwd)

    def __repr__(self):
        return f"<User {self.id}-{self.name}>"



class MyModelView(ModelView):

    def is_accessible(self):
        return flask_login.current_user.is_authenticated and flask_login.current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('signin', next=request.url))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated and flask_login.current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('signin', next=request.url))

