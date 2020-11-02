from flask import Flask
from config import Config
from flask_admin import Admin

#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_login import LoginManager
import flask_sqlalchemy
import flask_migrate


admin = Admin(template_mode='bootstrap4')
login_mgr = LoginManager()

app=Flask(__name__)
app.config.from_object(Config)



db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
login_mgr.init_app(app)


from app import views
from app import models

admin.init_app(app, index_view=models.MyAdminIndexView())

@login_mgr.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)
