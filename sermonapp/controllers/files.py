#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,E1101,W0613
from flask import make_response
from sermonapp import app
from sermonapp.models import File, FileData
from sermonapp.utils import not_found


@app.route('/files/<file_id>/<file_name>')
def get_file(file_id, file_name):
    file = File.query.get(file_id)
    if not file:
        return not_found()
    file_data = FileData.query.get(file.file_data_id)
    if not file_data:
        return not_found()
    response = make_response(file_data.data)
    response.headers['Content-Type'] = file.content_type
    content_disposition = file.content_type.startswith('image') and 'inline' or 'attachment'
    response.headers['Content-Disposition'] = '%s; filename=%s' % (content_disposition, file.name)
    response.headers['Cache-Control'] = 'public, max-age=31536000'
    return response
