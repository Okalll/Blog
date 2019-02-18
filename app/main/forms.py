from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import *


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')