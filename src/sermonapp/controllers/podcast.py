#!/usr/bin/python
# -*- coding: utf-8 -*-
# See documentation: https://github.com/lkiesow/python-feedgen
# Alternative: http://podgen.readthedocs.io/en/latest/
from feedgen.feed import FeedGenerator
from sermonapp import app

@app.route('/podcast.xml')
def podcast_index():
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.podcast.itunes_category('Technology', 'Podcasting')

    fg.id('http://lernfunk.de/media/654321')
    fg.title('Some Testfeed')
    fg.author( {'name':'John Doe','email':'john@example.de'} )
    fg.link( href='http://example.com', rel='alternate' )
    fg.logo('https://www.liebherr.com/media/global/img/svg/logo_ci_liebherr.svg')
    fg.subtitle('This is a cool feed!')
    fg.link( href='http://larskiesow.de/test.atom', rel='self' )
    fg.language('en')

    fe = fg.add_entry()
    fe.id('http://desktop-a59bqic:5000/files/61dfc2b84d2c45b9945a6232893050ea/02_-_Ein_neuer_Fall.mp3')
    fe.title('The First Episode')
    fe.description('Enjoy our first episode.')
    fe.enclosure('http://desktop-a59bqic:5000/files/61dfc2b84d2c45b9945a6232893050ea/02_-_Ein_neuer_Fall.mp3', 0, 'audio/mpeg')

    return fg.rss_str(pretty=True)
