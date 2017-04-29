#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_restful import Resource
from sermonapp import api
from sermonapp.models import Category


class CategoriesListApiResource(Resource):

    def get(self):
        categories = Category.query.all()
        return [c.get_dict() for c in categories]


class CategoryApiResource(Resource):

    def get(self, id):
        return Category.query.get(id).get_dict()


api.add_resource(CategoriesListApiResource, '/api/categories')
api.add_resource(CategoryApiResource, '/api/category/<id>')
