from andrimar_site.extensions import db
from chalice import init_app
from andrimar_site.blog.models import Tag, Post
from andrimar_site.auth.models import User

if __name__ == '__main__':
    app = init_app()
    with app.test_request_context():
        db.create_all()
        tag1 = Tag('programming')
        tag2 = Tag('rant')
        db.session.add(tag1)
        db.session.add(tag2)
        post = Post( 'This is a title', 'The classic hello world here.')
        post.tags = [tag1, tag2]
        db.session.add(post)
        user = User('andrimar', 'testpass')
        db.session.add(user)
        db.session.commit()
    print 'Initialized an empty db using the following connection string: %s' % app.config['SQLALCHEMY_DATABASE_URI']
