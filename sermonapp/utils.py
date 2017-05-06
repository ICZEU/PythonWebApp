#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
from flask import jsonify
from flask import make_response
from flask import request
from werkzeug.utils import secure_filename
from sermonapp.models import File
from sermonapp.models import FileData


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
    

def get_file_from_request(key):
    """Get an uploaded file from the current request as File object."""
    if key in request.files and request.files[key].filename:
        file = request.files[key]
        filename = secure_filename(file.filename)
        input_stream = BytesIO()
        file.save(input_stream)
        file_data = input_stream.getvalue()
        return File(filename, file.content_type, file_data)
    return None