"""Custom template filters for Jinja2"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=C0111
from sermonapp import app

@app.template_filter('date')
def format_datetime_short(value):
    if not value:
        return str()
    return value.strftime(app.config['DATE_FORMAT'])

@app.template_filter('datetime')
def format_datetime_full(value):
    if not value:
        return str()
    return value.strftime(app.config['DATETIME_FORMAT'])


@app.template_filter('human_filesize')
def human_filesize(size_bytes):
    """
    format a size in bytes into a 'human' file size, e.g. bytes, KB, MB, GB, TB, PB
    Note that bytes/KB will be reported in whole numbers but MB and above will have
    greater precision e.g. 1 byte, 43 bytes, 443 KB, 4.3 MB, 4.43 GB, etc
    """
    if size_bytes == 1:
        # because I really hate unnecessary plurals
        return "1 byte"
    suffixes_table = [('bytes', 0), ('KB', 0), ('MB', 1), ('GB', 2), ('TB', 2), ('PB', 2)]
    num = float(size_bytes)
    precision = None
    suffix = None
    for suffix, precision in suffixes_table:
        if num < 1024.0:
            break
        num /= 1024.0
    if precision == 0:
        formatted_size = "%d" % num
    else:
        formatted_size = str(round(num, ndigits=precision))
    return "%s %s" % (formatted_size, suffix)
