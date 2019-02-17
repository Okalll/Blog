from flask import render_template
from app import app
from .forms import BlogFOrm
from .models import blog
Blog= blog.Blog

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/blog/new/title', methods = ['GET','POST'])
def new_blog(title):
    form = blogForm()


    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        new_blog = blog(title,blog)
        new_blog.save_blog()
        return redirect(url_for('blog',title= title ))

