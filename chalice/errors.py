from flask import render_template
from chalice.extensions import app

@app.errorhandler(404)
def show_404(error):
    return render_template('404.html'), 404

