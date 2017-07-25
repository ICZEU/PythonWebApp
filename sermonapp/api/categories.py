#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from werkzeug.exceptions import NotFound, BadRequest
from flask_restplus import Namespace, Resource, fields
from sermonapp import db
from sermonapp.api import api
from sermonapp.models import Category
from sermonapp.schemas import category_schema

ns = Namespace('categories', description='Manage categories for sermons.')

category = ns.model('Category', {
    'id': fields.String(required=True),
    'name': fields.String(required=True, description='Category name'),
    'created_at': fields.DateTime()
})

category_edit = ns.model('Category', {
    'name': fields.String(required=True, description='Category name')
})


@ns.route('/')
class CategoryList(Resource):
    @ns.marshal_list_with(category)
    def get(self):
        '''List all categories'''
        return Category.query.all()

    @ns.expect(category_edit)
    @ns.marshal_with(category, code=201)
    @ns.response(400, 'Model validation failed.')
    def post(self):
        '''Create a new category'''
        if 'id' in api.payload:
            raise BadRequest("Please use the PUT method at endpoint /categories/<id> to update data.")
        if not 'name' in api.payload:
            raise BadRequest()
        model = category_schema.load(api.payload).data
        db.session.add(model)
        db.session.commit()
        return model, 201


@ns.route('/<id>')
@ns.param('id', 'The category identifier')
@ns.response(404, 'Category not found')
class CategoryItem(Resource):
    @ns.marshal_with(category)
    def get(self, id):
        '''Get a certain category by id.'''
        model = Category.query.get(id)
        if not model:
            raise NotFound()
        return model

    @ns.expect(category_edit)
    @ns.marshal_with(category)
    @ns.response(404, 'Category not found')
    @ns.response(400, 'Model validation failed.')
    def put(self, id):
        '''Update a certain category.'''
        if not 'name' in api.payload:
            raise BadRequest()
        model = Category.query.get(id)
        if not model:
            raise NotFound()
        model.name = api.payload['name']
        db.session.commit()
        return model

    @ns.response(204, 'Category deleted')
    @ns.response(404, 'Category not found')
    def delete(self, id):
        '''Delete a category by id'''
        model = Category.query.get(id)
        if not model:
            raise NotFound()
        db.session.delete(model)
        db.session.commit()
        return '', 204
