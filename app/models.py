from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        # return f'User {self.username}'
        return '<User %r>' % self.username


class Blog:

    def save_blog(self):
        Blog.all_blogs.append(self)


@classmethod
def clear_blogs(cls):
    Blog.all_blogs.clear()


@classmethod
def get_blogs(cls, title):

 response = []

class Login:
    login = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        1


class Register:
    register = []

    def __init__(self, username, email, password, confirmpassword):
        self.username = username
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword
