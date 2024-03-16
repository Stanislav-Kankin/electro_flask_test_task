from flask_sqlalchemy import SQLAlchemy
from webapp.app import app

db = SQLAlchemy(app)


class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
