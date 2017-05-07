#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['VIDEO_PROVIDERS'] = ['YouTube', 'Vimeo']


# Keep this really secret. Used to sign the cookies.
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Database access with SQLAlchemy.
# Configuration: http://flask-sqlalchemy.pocoo.org/2.1/config/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sermonapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

# Object serialization and deserialization
# https://flask-marshmallow.readthedocs.io/en/latest/
# Order matters: Initialize SQLAlchemy before Marshmallow
ma = Marshmallow(app)

import sermonapp.models
import sermonapp.controllers
import sermonapp.template_filters

# Initialize the database
from sermonapp.database import ensure_database
ensure_database()

# Date and Time settings
app.config['DATE_FORMAT'] = '%d.%m.%Y'
app.config['DATETIME_FORMAT'] = '%d.%m.%Y %H:%M Uhr'

# Convert the python datetime format to kendo datetime
# format for the client-side date picker.
from sermonapp.utils import to_kendo_datetime_format
app.config['KENDO_DATE_FORMAT'] = to_kendo_datetime_format(app.config['DATE_FORMAT'])
