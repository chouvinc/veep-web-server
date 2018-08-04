from datetime import datetime
from app import db
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# A quick note about __repr__ : this is an optional method to implement -- all it does is make
# logging database objects pretty (I believe it just prints a reference usually).

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    team = db.Column(db.String(128), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # TODO: run the url through a compressor if the link is very long
    photo_url = db.Column(db.String(120), unique=True, default='n/a')
    role = db.Column(db.String(120), index=True)
    is_executive = db.Column(db.Boolean, index=True, default=False)
    username = db.Column(db.String(120), index=True, unique=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    tags = db.Column(db.String(128), index=True)
    description = db.Column(db.String(16384), index=True)
    is_veep_x = db.Column(db.Boolean, default=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    location = db.Column(db.String(128), index=True)
    desc = db.Column(db.String(2048), index=True)

    def __repr__(self):
        return '<Event {}>'.format(self.body)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))