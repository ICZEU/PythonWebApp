#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# RESTful API
api = Api(app)

# Database access with SQLAlchemy.
# Configuration: http://flask-sqlalchemy.pocoo.org/2.1/config/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sermonapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import sermonapp.models
import sermonapp.controllers
import sermonapp.api

# Initialize the database
from sermonapp.database import ensure_database
ensure_database()
