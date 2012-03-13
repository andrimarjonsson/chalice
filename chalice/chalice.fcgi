#!/usr/bin/python

# First a little path hack
import sys
sys.path.append('../')

from flup.server.fcgi import WSGIServer
from chalice import create_app

if __name__ == "__main__":
    app = create_app()
    WSGIServer(app).run()
