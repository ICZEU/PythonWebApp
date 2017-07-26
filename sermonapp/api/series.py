#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from werkzeug.exceptions import NotFound, BadRequest
from flask_restplus import Namespace, Resource, fields
from sermonapp import db
from sermonapp.api import api
from sermonapp.models import Series

ns = Namespace('series', description='Manage series of sermons.')

series_fields = {
    'id': fields.Integer(required=True),
    'title': fields.String(required=True, description='Series name'),
    'description': fields.String(description='Short description.'),
    'image_id': fields.String(description='File id of the preview image. Upload an image against the /files endpoint before.'),
    'created_at': fields.DateTime()
}

series = ns.model('Series', series_fields)

# Fields that can be edited.
series_edit_fields = dict(series_fields)
series_edit_fields.pop('id')
series_edit_fields.pop('created_at')
series_edit = ns.model('Series', series_edit_fields)


@ns.route('/')
class SeriesList(Resource):
    @ns.marshal_list_with(series)
    def get(self):
        '''List all series'''
        return Series.query.all()

    @ns.expect(series_edit)
    @ns.marshal_with(series, code=201)
    @ns.response(400, 'Model validation failed.')
    def post(self):
        '''Create a new series'''
        if 'id' in api.payload:
            raise BadRequest("Please use the PUT method at endpoint /categories/<id> to update data.")
        if not 'title' in api.payload:
            raise BadRequest()
        model = Series()
        model.title = api.payload['title']
        model.description = api.payload['description']
        model.image_id = api.payload['image_id']
        db.session.add(model)
        db.session.commit()
        return model, 201


@ns.route('/<id>')
@ns.param('id', 'The series identifier')
@ns.response(404, 'Series not found')
class SeriesItem(Resource):
    @ns.marshal_with(series)
    def get(self, id):
        '''Get a certain series by id.'''
        model = Series.query.get(id)
        if not model:
            raise NotFound()
        return model

    @ns.expect(series_edit)
    @ns.marshal_with(series)
    @ns.response(404, 'Series not found')
    @ns.response(400, 'Model validation failed.')
    def put(self, id):
        '''Update a certain series.'''
        if not 'title' in api.payload:
            raise BadRequest()
        model = Series.query.get(id)
        if not model:
            raise NotFound()
        model.title = api.payload['title']
        model.description = api.payload['description']
        model.image_id = api.payload['image_id']
        db.session.commit()
        return model

    @ns.response(204, 'Series deleted')
    @ns.response(404, 'Series not found')
    def delete(self, id):
        '''Delete a series by id'''
        model = Series.query.get(id)
        if not model:
            raise NotFound()
        db.session.delete(model)
        db.session.commit()
        return '', 204
