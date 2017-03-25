#!/usr/bin/python
import sys
sys.path.insert(0, "venv/Lib/site-packages")

def print_error(exception):
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers
    print "<h1>Internal Server Error</h1>"
    print exception

try:

    # enable debugging
    import cgitb
    cgitb.enable()

    from wsgiref.handlers import CGIHandler
    from sermonapp import app

    CGIHandler().run(app)

except Exception as ex:
   print_error(ex)