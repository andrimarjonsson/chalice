#!/usr/bin/python

# First a little path hack
import sys
#sys.path.append('../')

from flup.server.fcgi import WSGIServer
from chalice import init_app

app = init_app()
WSGIServer(app).run()
