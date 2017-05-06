#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101
from flask import render_template, request, redirect, url_for
from sermonapp import app, db
from sermonapp.utils import not_found, get_file_from_request
from sermonapp.models import Speaker, Series, Category
from sqlalchemy.orm import load_only


@app.route('/sermons')
def sermon_index():
    return render_template('sermons/index.html')


@app.route('/sermons/add')
def sermon_add():
    speakers = (
        db.session
        .query(Speaker.id, Speaker.firstname, Speaker.lastname)
        .order_by(Speaker.lastname))
    series = (
        db.session
        .query(Series.id, Series.title)
        .order_by(Series.title))
    categories = (
        db.session
        .query(Category.id, Category.name)
        .order_by(Category.name))
    return render_template('sermons/edit.html',
        page_title="Predigt hinzufügen", speakers=speakers,
        series=series, categories=categories,
        video_providers = app.config['VIDEO_PROVIDERS'])


@app.route('/sermons/edit')
def sermon_edit():
    return render_template('sermons/edit.html', page_title="Predigt bearbeiten")
