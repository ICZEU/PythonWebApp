#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, abort, jsonify
from sermonapp import app, db
from sermonapp.utils import not_found, bad_request
from sermonapp.models import Category
from sermonapp.schemas import category_schema, categories_schema


@app.route('/categories')
def category_index():
    return render_template('categories/index.html', categories=Category.query.all())


@app.route('/api/categories')
def category_list():
    categories = Category.query.all()
    return categories_schema.jsonify(categories)


@app.route('/api/categories/<int:id>')
def category_detail(id):
    category = Category.query.get(id)
    if not category:
        return not_found()
    return category_schema.jsonify(category)


@app.route('/api/categories', methods=['POST'])
def category_new():
    if not request.json or not 'name' in request.json or 'id' in request.json:
        abort(400)
    category = category_schema.load(request.json).data
    db.session.add(category)
    try:
        db.session.commit()
    except Exception as error:
        return bad_request(error)
    return category_schema.jsonify(category), 201


@app.route('/api/categories/<int:id>', methods=['PUT'])
def category_update(id):
    category = Category.query.get(id)
    if not category:
        return not_found()
    if not request.json or not 'name':
        abort(400)
    category.name = request.json['name']
    db.session.commit()
    return category_schema.jsonify(category)


@app.route('/api/categories/<int:id>', methods=['DELETE'])
def category_delete(id):
    category = Category.query.get(id)
    if not category:
        return not_found()
    db.session.delete(category)
    db.session.commit()
    return jsonify({'result': True})
