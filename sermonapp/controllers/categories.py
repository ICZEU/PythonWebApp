#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from flask import jsonify
from sermonapp import app
from sermonapp.models import Category

@app.route('/categories')
def category_index():
    return render_template('categories/index.html', categories = Category.query.all())

# @app.route('/api/categories')
# def category_all():
#     categories = Category.query.all()    
#     return jsonify([c.get_dict() for c in categories])