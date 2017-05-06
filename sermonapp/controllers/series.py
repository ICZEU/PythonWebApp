#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for
from sermonapp import app, db
from sermonapp.models import Series
from sermonapp.utils import not_found
from sermonapp.utils import get_file_from_request
from sermonapp.models import FileData
from sermonapp.database import delete_file


@app.route('/series')
def series_index():
    series = Series.query.all()
    return render_template('series/index.html', series=series)


@app.route('/series/add', methods=['GET', 'POST'])
def series_add():
    if request.method == 'POST':
        series = Series()
        series.image = get_file_from_request('image')
        series.title = request.form['title']
        series.description = request.form['description']
        db.session.add(series)
        db.session.commit()
        return redirect(url_for('series_index'))
    return render_template('series/edit.html', series=None, page_title="Serie hinzufügen")


@app.route('/series/<series_id>/edit', methods=['GET', 'POST'])
def series_edit(series_id):
    series = Series.query.get(series_id)
    if not series:
        return not_found()
    if request.method == 'POST':
        previous_image = series.image
        series.image = get_file_from_request('image')
        series.title = request.form['title']
        series.description = request.form['description']
        db.session.commit()
        # Clean up previous image.
        if previous_image:
            delete_file(previous_image)
        return redirect(url_for('series_index'))
    return render_template('series/edit.html',
        series=series, page_title="Serie bearbeiten")


@app.route('/series/<series_id>/delete', methods=['GET', 'POST'])
def series_delete(series_id):
    series = Series.query.get(series_id)
    if not series:
        return not_found()
    if series.image:
        delete_file(series.image)
    db.session.delete(series)
    db.session.commit()
    return redirect(url_for('series_index'))
