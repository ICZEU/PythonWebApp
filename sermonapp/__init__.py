#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

import sermonapp.views
from sermonapp.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()