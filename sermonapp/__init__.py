#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database access with SQLAlchemy.
# Configuration: http://flask-sqlalchemy.pocoo.org/2.1/config/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sermonapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Object serialization and deserialization
# https://flask-marshmallow.readthedocs.io/en/latest/
# Order matters: Initialize SQLAlchemy before Marshmallow
ma = Marshmallow(app)

import sermonapp.models
import sermonapp.controllers

# Initialize the database
from sermonapp.database import ensure_database
ensure_database()
