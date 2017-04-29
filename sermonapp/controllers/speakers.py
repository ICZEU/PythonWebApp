#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from sermonapp import app

@app.route('/speakers')
def speaker_index():
    return render_template('speakers/index.html')

@app.route('/speakers/add')
def speaker_add():
    return render_template('speakers/edit.html', page_title = "Prediger hinzufügen")

@app.route('/speakers/edit')
def speaker_edit():
    return render_template('speakers/edit.html', page_title = "Bearbeiten")
