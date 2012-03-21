from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask.ext.login import login_required
from chalice.blog.models import Post, Tag
from chalice.helpers import generate_taglist
from chalice.extensions import db

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
    posts = Post.query.filter(Post.tags.any(name = tag)).all()
    return render_template('taggedposts.html', posts = posts, tag = tag)

# -- Admin section
# -- TODO: Add error handling

@blog.route('/post/new', methods = ['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post = Post(request.form['title'], request.form['text'])
        post.tags = generate_taglist(request.form['tags'])
        db.session.add(post)
        db.session.commit()
        flash('Your post has been added.')
        return redirect(url_for('blog.show_posts'))
    return render_template('new_post.html')

@blog.route('/tag/new', methods = ['GET', 'POST'])
@login_required
def new_tag():
    if request.method == 'POST':
        tag = Tag(request.form['name'])
        db.session.add(tag)
        db.session.commit()
        flash('Your tag has been added.')
        return redirect(url_for('blog.show_tags'))
    return render_template('new_tag.html')

