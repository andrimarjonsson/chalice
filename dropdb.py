from andrimar_site.extensions import db
from chalice import init_app

if __name__ == '__main__':
    app = init_app()
    with app.test_request_context():
        db.drop_all()
    print 'Dropped the db using the following connection string: %s' % app.config['SQLALCHEMY_DATABASE_URI']

