#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import environ
from sermonapp import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, debug=True, threaded=True)
    