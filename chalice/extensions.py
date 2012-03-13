from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

__all__ = ['app', 'db', 'lm']

# Create the base application object.
app = Flask("chalice")

# Create the flask.sqlalchemy object 
db = SQLAlchemy()

# Create the flask.ext.login obejct
lm = LoginManager()

