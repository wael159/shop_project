
from app import db
import flask_login
import werkzeug
from sqlalchemy.ext.hybrid import hybrid_property
from app.utils import ModelMixin

#class all_products(db.Model): # SQL Table
    # Create attributes (SQL columns)
#    id = db.Column(db.Integer(), primary_key=True) # By default autoincremented
#    name = db.Column(db.String(64))
#    price  = db.Column(db.Integer())
#    stock_quantity = db.Column(db.Integer())
#    category=db.Column(db.String(64))


class books(db.Model,ModelMixin): # SQL Table
    # Create attributes (SQL columns)
     # By default autoincremented
    name = db.Column(db.String(64))
    price  = db.Column(db.Integer())
    stock_quantity = db.Column(db.Integer())
    category=db.Column(db.String(64))
    description=db.Column(db.String(64))
    author_name=db.Column(db.String(64))
    year=db.column(db.String(64))




class User(db.Model, ModelMixin, flask_login.UserMixin): # SQL Table

    # Create attributes (SQL columns)
    id = db.Column(db.Integer(), primary_key=True)  # By default autoincremented
    name             = db.Column(db.String(64), nullable=False)
    _password_hash    = db.Column(db.String(256))

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

