#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
from datetime import datetime
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from werkzeug.utils import secure_filename
from sermonapp import app
from sermonapp.models import File


def not_found(error=None):
    """Return 404 not found."""
    status_code = 404
    error = error and str(error)
    if request_wants_json():
        return make_response(jsonify({'error': error or 'Not found'}), status_code)
    return abort(status_code, error)


def bad_request(error=None):
    """Return 400 bad request."""
    status_code = 400
    error = error and str(error)
    if request_wants_json():
        return make_response(jsonify({'error': error or 'Bad request'}), status_code)
    return abort(status_code, error)


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


def request_wants_json():
    """Returns if the request wants json as response."""
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


def to_kendo_datetime_format(datetime_format):
    """Convert a python datetime format (%d.%m.%Y) to a kendo datetime format (dd.MM.yyyy)."""
    return (datetime_format
            .replace('%Y', 'yyyy')
            .replace('%m', 'MM')
            .replace('%d', 'dd'))


def parse_date(date_string):
    """Parse a date string using the datetime format of the current application."""
    try:
        return datetime.strptime(date_string, app.config['DATE_FORMAT'])
    except ValueError:
        return None
