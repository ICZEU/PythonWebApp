#!/usr/bin/python
# -*- coding: utf-8 -*-
from sermonapp import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sermons')
def sermon_index():
    return render_template('sermon_index.html')

@app.route('/sermons/add')
def sermon_add():
    return render_template('sermon_edit.html', page_title = "Predigt hinzufügen")

@app.route('/sermons/edit')
def sermon_edit():
    return render_template('sermon_edit.html', page_title = "Predigt bearbeiten")

@app.route('/speakers')
def speaker_index():
    return render_template('speaker_index.html')

@app.route('/speakers/add')
def speaker_add():
    return render_template('speaker_edit.html', page_title = "Prediger hinzufügen")

@app.route('/speakers/edit')
def speaker_edit():
    return render_template('speaker_edit.html', page_title = "Bearbeiten")

@app.route('/series')
def series_index():
    return render_template('series_index.html')

@app.route('/series/add')
def series_add():
    return render_template('series_edit.html', page_title = "Serie hinzufügen")

@app.route('/series/edit')
def series_edit():
    return render_template('series_edit.html', page_title = "Serie bearbeiten")

@app.route('/categories')
def category_index():
    return render_template('category_index.html')