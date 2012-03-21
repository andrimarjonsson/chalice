from chalice.extensions import db
from chalice import init_app
from chalice.blog.models import Tag, Post
from chalice.auth.models import User

if __name__ == '__main__':
    app = init_app()
    with app.test_request_context():
        db.create_all()
        post = Post( 'This is a title', 'The classic hello world here.')
        post.tags = ['rant', 'programming']
        db.session.add(post)
        user = User('andrimar', 'testpass')
        db.session.add(user)
        db.session.commit()
    print 'Initialized an empty db using the following connection string: %s' % app.config['SQLALCHEMY_DATABASE_URI']
