from chalice.extensions import db
from flask.ext.login import UserMixin

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    # -- Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(30), nullable = False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %s>' % self.name
