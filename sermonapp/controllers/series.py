#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from sermonapp import app

@app.route('/series')
def series_index():
    return render_template('series/index.html')

@app.route('/series/add')
def series_add():
    return render_template('series/edit.html', page_title = "Serie hinzufügen")

@app.route('/series/edit')
def series_edit():
    return render_template('series/edit.html', page_title = "Serie bearbeiten")

