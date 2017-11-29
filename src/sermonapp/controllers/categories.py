#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from flask import render_template
from sermonapp import app
from sermonapp.models import Category


@app.route('/categories')
def category_index():
    return render_template('categories/index.html', categories=Category.query.all())
