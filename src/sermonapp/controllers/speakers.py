#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from sermonapp import app, db
from sermonapp.models import Speaker
from sermonapp.models import FileData
from sermonapp.utils import not_found
from sermonapp.utils import get_file_from_request
from sermonapp.database import delete_file

@app.route('/speakers')
def speaker_index():
    speakers = Speaker.query.all()
    return render_template('speakers/index.html', speakers=speakers)


@app.route('/speakers/add', methods=['GET', 'POST'])
def speaker_add():
    if request.method == 'POST':
        speaker = Speaker()
        speaker.firstname = request.form['firstname']
        speaker.lastname = request.form['lastname']
        speaker.position = request.form['position']
        speaker.description = request.form['description']
        speaker.image = get_file_from_request('image')
        db.session.add(speaker)
        db.session.commit()
        return redirect(url_for('speaker_index'))
    return render_template('speakers/edit.html', model=None, page_title="Prediger hinzufügen")


@app.route('/speakers/<speaker_id>/edit', methods=['GET', 'POST'])
def speaker_edit(speaker_id):
    speaker = Speaker.query.get(speaker_id)
    if not speaker:
        return not_found()
    if request.method == 'POST':
        previous_image = speaker.image
        speaker.firstname = request.form['firstname']
        speaker.lastname = request.form['lastname']
        speaker.position = request.form['position']
        speaker.description = request.form['description']
        speaker.image = get_file_from_request('image')
        db.session.commit()
        # Clean up previous image.
        if previous_image:
            delete_file(previous_image)
        return redirect(url_for('speaker_index'))
    return render_template('speakers/edit.html',
        model=speaker, page_title="Bearbeiten")


@app.route('/speakers/<speaker_id>/delete')
def speaker_delete(speaker_id):
    speaker = Speaker.query.get(speaker_id)
    if not speaker:
        return not_found()
    if speaker.image:
        delete_file(speaker.image)
    db.session.delete(speaker)
    db.session.commit()
    return redirect(url_for('speaker_index'))