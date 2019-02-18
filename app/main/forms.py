from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import Required, Email, EqualTo

class BlogForm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')