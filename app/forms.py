from flask_wtf import FlaskForm
from wtforms import Form,StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogFOrm(FlaskForm):

    title = StringField('Blog title',validators=[Required()])
    blog = TextAreaField('Blog', validators=[Required()])
    submit = SubmitField('Submit')