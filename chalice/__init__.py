from chalice.blog import blog
from chalice.pages import pages
from chalice.auth import auth
from chalice.upload import upload
from chalice.extensions import db, app, lm

import chalice.filters
import chalice.errors

import default_config

__all__ = ['init_app']

# -- TODO: Need to find a better spot for this.
@app.route('/markdown_preview', methods=['POST'])
def preview():
    return Markup(markup(request.values['data']))

def init_app():
    app.config.from_object(default_config)

    app.register_blueprint(pages)
    app.register_blueprint(blog)
    app.register_blueprint(auth)
    app.register_blueprint(upload, url_prefix='/upload')

    db.init_app(app)
    lm.setup_app(app)

    return app
