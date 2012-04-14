from flask import Markup
from chalice.extensions import app
from chalice.helpers import markup

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
