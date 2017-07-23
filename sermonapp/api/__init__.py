#!/usr/bin/python
# -*- coding: utf-8 -*-
"""REST API for SermonApp realized with Flask.RESTPlus.

See documentation:
    http://flask-restplus.readthedocs.io/en/latest/
"""
from flask import Blueprint
from flask_restplus import Api
from .categories import api as category_api

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(
    api_v1,
    title='SermonApp API',
    version='1.0',
    description='REST API for managing the sermons of your church.'
)

api.add_namespace(category_api)
