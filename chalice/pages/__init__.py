from flask import Blueprint, render_template
from flask import Markup
from chalice.helpers import markup

pages = Blueprint('pages', __name__, template_folder = 'templates')

@pages.route('/about')
def about():
    content = None
    with pages.open_resource('about.md') as f:
        content = Markup(markup(unicode(f.read(), "UTF-8")))
    return render_template('default_page.html', content = content, pagename = 'about me')

