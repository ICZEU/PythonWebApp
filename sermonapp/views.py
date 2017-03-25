from sermonapp import app
from flask import render_template

#test

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sermons')
def sermons_index():
    return render_template('sermons.html')

@app.route('/speakers')
def speakers_index():
    return render_template('speakers.html')

@app.route('/series')
def series_index():
    return render_template('series.html')

@app.route('/categories')
def categories_index():
    return render_template('categories.html')