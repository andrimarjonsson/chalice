from flask import Blueprint, render_template
from flask import Markup
import markdown

pages = Blueprint('pages', __name__, template_folder = 'templates')

@pages.route('/about')
def about():
    content = None
    with pages.open_resource('about.md') as f:
        content = Markup(markdown.markdown(unicode(f.read(), 'UTF-8'), extensions = ['codehilite', 'html_tidy'], output_format = 'html5'))
    return render_template('default_page.html', content = content, pagename = 'about me')

