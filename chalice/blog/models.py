from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime
from chalice.extensions import db
from chalice.helpers import slugify

class Post(db.Model):

    __tablename__ = 'posts'

    # -- Columns
    id = db.Column(db.Integer, primary_key = True)
    _title = db.Column('title', db.String(255), nullable = False)
    _slug = db.Column('slug', db.String(255), unique = True, nullable = False)
    text = db.Column(db.Text)
    create_date = db.Column(db.DateTime)
    edit_date = db.Column(db.DateTime)

    # -- Relationships
    # Many to many - Post <-> Tag
    tags = db.relationship('Tag', secondary='post_tags', backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.create_date = datetime.now()
        self.edit_date = datetime.now()

    @hybrid_property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self._slug = slugify(unicode(title))

    @hybrid_property
    def slug(self):
        return self._slug

    def __repr__(self):
        return '<Post %s>' % self.slug

class Tag(db.Model):

    __tablename__ = 'tags'

    # -- Columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True, nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Tag %s>' % self.name

# Association table for Post <-> Tag
post_tags = db.Table('post_tags', db.Model.metadata,
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id', ondelete='CASCADE')),
    db.Column('tag_id',  db.Integer, db.ForeignKey('tags.id',  ondelete='CASCADE')))
