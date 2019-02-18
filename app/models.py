from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(8))
    email = db.Column(db.String(255), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

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


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    category = db.Column(db.String(255), nullable=False)


def save_blog(self):
        Blog.all_blogs.append(self)


@classmethod
def clear_blogs(cls):
    Blog.all_blogs.clear()


@classmethod
def get_blogs(cls, title):

 response = []

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

