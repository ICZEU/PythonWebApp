#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0111,E1101,W0613
# See documentation: http://demos.telerik.com/kendo-ui/upload/chunkupload
import os
import json
from flask import request, jsonify
from sermonapp import app
from sermonapp.schemas import UploadChunkSchema
from sermonapp.utils import get_file_from_request

TEMP_FOLDER = "c:/temp" # TODO: Move to config file

schema = UploadChunkSchema()

@app.route('/upload', methods=['POST'])
def upload():
    if not 'metadata' in request.form or not 'files' in request.files:
        return # TODO: Save files
    dic = json.loads(request.form['metadata'])
    metadata = schema.load(dic).data
    blob = get_file_from_request('files')
    append_to_file(metadata, blob)
    uploaded = metadata.total_chunks - 1 <= metadata.chunk_index
    return jsonify({ 'uploaded': uploaded, 'fileUid': metadata.upload_uid })


def append_to_file(metadata, blob):
    """Append the chunk to a temporary file"""
    full_path = os.path.join(TEMP_FOLDER, metadata.file_name)
    with open(full_path, 'ab') as file:
        file.write(blob.file_data.data)


@app.route('/remove')
def remove():
    return "Not implemented"
