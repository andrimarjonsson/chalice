from flask import Blueprint, render_template, abort
from flask.ext.login import login_required
from chalice.blog.models import Post, Tag

blog = Blueprint('blog', __name__, template_folder = 'templates')

@blog.route('/')
@blog.route('/posts')
def show_posts():
    posts = Post.query.order_by(Post.create_date.desc()).all()
    return render_template('posts.html', posts = posts)

@blog.route('/post/<slug>')
def show_post(slug):
    post = Post.query.filter_by(slug = slug).first_or_404()
    return render_template('post.html', post = post)

@blog.route('/tags')
def show_tags():
    tags = Tag.query.order_by(Tag.name.desc()).all()
    return render_template('tags.html', tags = tags)

@blog.route('/tags/<tag>')
def show_posts_with_tag(tag):
    posts = Post.query.filter(Post.tags.any(name=tag)).all()
    return render_template('taggedposts.html', posts = posts, tag = tag)

