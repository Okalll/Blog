from flask import render_template,url_for,request
from flask_login import login_required
from ..models import Blog
from .forms import BlogForm
from . import main
from .. import db


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/blog/new/title', methods = ['GET','POST'])
@login_required
def new_pitch(title):
    '''
    Function that creates new pitches
    '''
    form = BlogForm()

    if form.validate_on_submit():
        blog = form.content.data
        category = form.category.data
        new_blog = blog(blog=blog, category=category)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form=form, category=category)

