#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from werkzeug.exceptions import NotFound, BadRequest
from flask_restplus import Namespace, Resource, fields
from sermonapp import db
from sermonapp.api import api
from sermonapp.models import Speaker

ns = Namespace('speakers', description='Manage speakers.')

speaker_fields = {
    'id': fields.Integer(required=True),
    'lastname': fields.String(required=True, description='Last name'),
    'firstname': fields.String(required=True, description='First name'),
    'position': fields.String(description='Position, Job Title, etc.'),
    'description': fields.String(description='Short description.'),
    'image_id': fields.String(description='File id of the preview image. Upload an image against the /files endpoint before.'),
    'created_at': fields.DateTime()
}

speaker = ns.model('Speaker', speaker_fields)

# Fields that can be edited.
speaker_edit_fields = dict(speaker_fields)
speaker_edit_fields.pop('id')
speaker_edit_fields.pop('created_at')
speaker_edit = ns.model('Speaker', speaker_edit_fields)


@ns.route('/')
class SpeakerList(Resource):
    @ns.marshal_list_with(speaker)
    def get(self):
        '''List all speakers'''
        return Speaker.query.all()

    @ns.expect(speaker_edit)
    @ns.marshal_with(speaker, code=201)
    @ns.response(400, 'Model validation failed.')
    def post(self):
        '''Create a new speaker'''
        if 'id' in api.payload:
            raise BadRequest("Please use the PUT method at endpoint /speakers/<id> to update data.")
        if not 'lastname' in api.payload or not 'firstname' in api.payload:
            raise BadRequest()
        model = Speaker()
        model.lastname = api.payload['lastname']
        model.firstname = api.payload['firstname']
        model.position = api.payload['position']
        model.description = api.payload['description']
        model.image_id = api.payload['image_id']
        db.session.add(model)
        db.session.commit()
        return model, 201


@ns.route('/<id>')
@ns.param('id', 'The speaker identifier')
@ns.response(404, 'Speaker not found')
class SpeakerItem(Resource):
    @ns.marshal_with(speaker)
    def get(self, id):
        '''Get a certain speaker by id.'''
        model = Speaker.query.get(id)
        if not model:
            raise NotFound()
        return model

    @ns.expect(speaker_edit)
    @ns.marshal_with(speaker)
    @ns.response(404, 'Speaker not found')
    @ns.response(400, 'Model validation failed.')
    def put(self, id):
        '''Update a certain speaker.'''
        if not 'lastname' in api.payload or not 'firstname' in api.payload:
            raise BadRequest()
        model = Speaker.query.get(id)
        if not model:
            raise NotFound()
        model.lastname = api.payload['lastname']
        model.firstname = api.payload['firstname']
        model.position = api.payload['position']
        model.description = api.payload['description']
        model.image_id = api.payload['image_id']
        db.session.commit()
        return model

    @ns.response(204, 'Speaker deleted')
    @ns.response(404, 'Speaker not found')
    def delete(self, id):
        '''Delete a speaker by id'''
        model = Speaker.query.get(id)
        if not model:
            raise NotFound()
        db.session.delete(model)
        db.session.commit()
        return '', 204
