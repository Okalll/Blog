from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required
from ..models import User,Blog
from .forms import UpdateProfile, BlogForm
from .. import db
from . import main


@main.route('/')
def index():
    '''
    View root page function that returns the home page and its data
    '''
    return render_template('index.html')


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    return render_template("Profile/profile.html", user=user)


@main.route('/user/<name>/update', methods=['GET', 'POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', name=user.username))

    return render_template('Profile/update.html', form=form)


@main.route('/user/<name>/update/pic', methods=['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))


@main.route('/blog/new/', methods=['GET', 'POST'])
@login_required
def new_blog():
    '''
    Function that creates new bloges
    '''
    form = BlogForm()

    if form.validate_on_submit():
        blog = form.content.data
        category = form.category.data
        new_blog = blog(blog=blog, category=category)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('new_blog.html', new_blog_form=form, category=category)
