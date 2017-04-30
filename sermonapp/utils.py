#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import jsonify
from flask import make_response

def not_found(error=None):
    """Return 404 not found."""
    if error:
        error = str(error)
    return make_response(jsonify({'error': error or 'Not found'}), 404)

def bad_request(error=None):
    """Return 404 bad request."""
    if error:
        error = str(error)
    return make_response(jsonify({'error': error or 'Bad request'}), 404)
    