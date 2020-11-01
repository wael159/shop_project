from flask import Flask
from config import Config

#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from flask_login import LoginManager
import flask_sqlalchemy
import flask_migrate

#db  = SQLAlchemy()
#migrate = Migrate()
login_mgr = LoginManager()

app=Flask(__name__)
app.config.from_object(Config)

#db.init_app(app)
#migrate.init_app(app, db)

db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
login_mgr.init_app(app)


from app import views
from app import models

@login_mgr.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)

print(app.config)
print(models)