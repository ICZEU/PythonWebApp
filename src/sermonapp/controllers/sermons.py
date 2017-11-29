#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=E1101,C0111
from flask import render_template, request, redirect, url_for
from sermonapp import app, db
from sermonapp.utils import not_found, parse_date, get_file_from_request
from sermonapp.database import delete_file
from sermonapp.models import Speaker, Series, Category, Sermon, Video


@app.route('/sermons')
def sermon_index():
    sermons = Sermon.query.order_by(Sermon.date.desc()).all()
    return render_template('sermons/index.html', sermons=sermons)


@app.route('/sermons/add', methods=['GET', 'POST'])
def sermon_add():
    if request.method == 'POST':
        sermon = Sermon()
        map_from_request(sermon)
        db.session.add(sermon)
        db.session.commit()
        return redirect(url_for('sermon_index'))
    return render_template(
        'sermons/edit.html', sermon=None,
        page_title="Predigt hinzufügen", **get_viewdata())


@app.route('/sermons/<sermon_id>/edit', methods=['GET', 'POST'])
def sermon_edit(sermon_id):
    sermon = Sermon.query.get(sermon_id)
    if not sermon:
        return not_found()
    if request.method == 'POST':
        prev_audiofile = sermon.audio_file
        map_from_request(sermon)
        db.session.commit()
        if prev_audiofile:
            delete_file(prev_audiofile)
        return redirect(url_for('sermon_index'))
    return render_template(
        'sermons/edit.html', sermon=sermon,
        page_title="Predigt bearbeiten", **get_viewdata())


@app.route('/sermons/<sermon_id>/delete')
def sermon_delete(sermon_id):
    sermon = Sermon.query.get(sermon_id)
    if not sermon:
        return not_found()
    db.session.delete(sermon)
    db.session.commit()
    return redirect(url_for('sermon_index'))


def get_viewdata():
    viewdata = dict()
    viewdata['speakers'] = (
        db.session
        .query(Speaker.id, Speaker.firstname, Speaker.lastname)
        .order_by(Speaker.lastname))
    viewdata['series'] = (
        db.session
        .query(Series.id, Series.title)
        .order_by(Series.title))
    viewdata['categories'] = (
        db.session
        .query(Category.id, Category.name)
        .order_by(Category.name))
    viewdata['video_providers'] = app.config['VIDEO_PROVIDERS']
    return viewdata


def map_from_request(sermon):
    sermon.title = request.form['title']
    sermon.date = parse_date(request.form['date'])
    sermon.speaker_id = request.form['speaker']
    sermon.series_id = request.form['series']
    sermon.category_id = request.form['category']
    sermon.bible_references = request.form['bible_references']
    sermon.published_from = parse_date(request.form['published_from'])
    sermon.published_until = parse_date(request.form['published_until'])
    sermon.hidden = bool(request.form.get('hidden'))
    if not sermon.video:
        sermon.video = Video()
    sermon.video.provider = request.form['video_provider']
    sermon.video.embed_id = request.form['embed_id']
    sermon.audio_file = get_file_from_request('audio_file')
