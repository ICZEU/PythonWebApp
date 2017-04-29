#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from sermonapp import app

@app.route('/sermons')
def sermon_index():
    return render_template('sermons/index.html')

@app.route('/sermons/add')
def sermon_add():
    return render_template('sermons/edit.html', page_title="Predigt hinzufügen")

@app.route('/sermons/edit')
def sermon_edit():
    return render_template('sermons/edit.html', page_title="Predigt bearbeiten")
