from flask import Flask, Blueprint, Markup
from flask.ext.login import login_required
from chalice.blog import blog
from chalice.pages import pages
from chalice.auth import auth
from chalice.extensions import db, app, lm
from chalice.helpers import markup

import default_config

__all__ = ['init_app']

# -- TODO: Need to find a better spot for this.
@app.template_filter()
def datetimeformat(datetime, timeago=True):
    readable = datetime.strftime('%Y-%m-%d @ %H:%M')
    if not timeago:
        return readable
    iso_format = datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    return Markup('<span class=timeago title="%s">%s</span>' % (iso_format, readable))

@app.template_filter()
def markitup(text):
    return Markup(markup(text))

@app.route('/markdown_preview', methods=['POST'])
def preview():
    return Markup(markup(request.values['data']))

def init_app():
    app.config.from_object(default_config)

    app.register_blueprint(pages)
    app.register_blueprint(blog)
    app.register_blueprint(auth)

    # Init init the db
    db.init_app(app)
    lm.setup_app(app)

    return app
