#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from sermonapp import app

@app.route('/')
def index():
    #return render_template('home/index.html')
    return redirect(url_for('sermon_index'))