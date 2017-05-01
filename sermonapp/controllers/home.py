#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
from sermonapp import app

@app.route('/')
def index():
    return render_template('home/index.html')