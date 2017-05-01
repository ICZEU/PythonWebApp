"""Custom template filters for Jinja2"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0111
from sermonapp import app

@app.template_filter('date')
def format_datetime_short(value):
    return value.strftime("%d.%m.%Y")

@app.template_filter('datetime')
def format_datetime_full(value):
    return value.strftime("%d.%m.%Y %H:%M Uhr")
