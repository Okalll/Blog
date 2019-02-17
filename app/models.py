class Blog:

    def save_blog(self):
        Blog.all_blogss.append(self)


@classmethod
def clear_blogs(cls):
    Blog.all_blogs.clear()


@classmethod
def get_blogs(cls, title):

 response = []

