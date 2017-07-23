#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from flask_restplus import Namespace, Resource, fields
from sermonapp.models import Category

api = Namespace('categories', description='Manage categories for sermons.')

category = api.model('Category', {
    'id': fields.String(required=True),
    'name': fields.String(required=True, description='Category name'),
    'created_at': fields.DateTime()
})


@api.route('/')
class CategoryList(Resource):
    @api.doc('list_categories')
    @api.marshal_list_with(category)
    def get(self):
        '''List all categories'''
        return Category.query.all()


@api.route('/<id>')
@api.param('id', 'The category identifier')
@api.response(404, 'Category not found')
class CategoryItem(Resource):
    @api.doc('get_category')
    @api.marshal_with(category)
    def get(self, id):
        '''Get a category by its identifier.'''
        item = Category.query.get(id)
        if item:
            return item
        api.abort(404)
