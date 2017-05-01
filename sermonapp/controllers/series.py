#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, flash, redirect, url_for
from sermonapp import app, db
from sermonapp.models import Series, File, FileData
from sermonapp.utils import not_found
from werkzeug.utils import secure_filename
from io import BytesIO

@app.route('/series')
def series_index():
    series = Series.query.all()
    return render_template('series/index.html', series=series)

@app.route('/series/add', methods=['GET', 'POST'])
def series_add():
    if request.method == 'POST':
        series = Series()
        if ('image' in request.files and request.files['image'].filename):
            # Get image from request.
            image = request.files['image']
            filename = secure_filename(image.filename)
            input_stream = BytesIO()
            image.save(input_stream)
            file_data = FileData(input_stream.getvalue())
            db.session.add(file_data)
            db.session.commit()
            series.file = File(filename, image.content_type, file_data)
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
        previous_image = None
        if ('image' in request.files and request.files['image'].filename):
            # Get image from request.
            image = request.files['image']
            filename = secure_filename(image.filename)
            input_stream = BytesIO()
            image.save(input_stream)
            file_data = FileData(input_stream.getvalue())
            db.session.add(file_data)
            db.session.commit()
            previous_image = series.file
            series.file = File(filename, image.content_type, file_data)
        
        series.title = request.form['title']
        series.description = request.form['description']
        db.session.commit()

        # Clean up previous image.
        if previous_image:
            db.session.delete(FileData.query.get(previous_image.file_data_id))
            db.session.delete(previous_image)
            db.session.commit()
        return redirect(url_for('series_index'))

    return render_template('series/edit.html',
        series=series, page_title="Serie bearbeiten")


@app.route('/series/<series_id>/delete', methods=['GET', 'POST'])
def series_delete(series_id):
    series = Series.query.get(series_id)
    if not series:
        return not_found()
    db.session.delete(series)
    db.session.commit()
    return redirect(url_for('series_index'))