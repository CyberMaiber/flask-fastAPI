from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    passwordhash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'User({self.username}, {self.email}, "HisPassword")'

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passwordhash = generate_password_hash(password,"md5")

    def __str__(self):
        return f'{self.username}, {self.email}, {self.passwordhash}'