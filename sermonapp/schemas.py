#!/usr/bin/python
# -*- coding: utf-8 -*-
from marshmallow import fields, post_load
from sermonapp import ma
from sermonapp.models import Category
from sermonapp.models import Series
from sermonapp.models import UploadChunk

class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category


class SeriesSchema(ma.ModelSchema):
    class Meta:
        model = Series


class UploadChunkSchema(ma.Schema):
    """Marshmallow schema for a file upload chunk"""
    chunkIndex = fields.Integer(attribute="chunk_index")
    contentType = fields.String(attribute="content_type")
    fileName = fields.String(attribute="file_name")
    totalFileSize = fields.Integer(attribute="total_file_size")
    totalChunks = fields.Integer(attribute="total_chunks")
    uploadUid = fields.UUID(attribute="upload_uid")

    @post_load
    def make_object(self, data):
        return UploadChunk(**data)