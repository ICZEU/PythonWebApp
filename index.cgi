#!/usr/bin/python
import sys
sys.path.insert(0, "venv/Lib/site-packages")

# enable debugging
import cgitb
cgitb.enable()

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)