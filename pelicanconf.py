#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pelican.settings import DEFAULT_CONFIG


AUTHOR = 'Luca Lanziani'
SITENAME = 'Luca Lanziani'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./pelican-themes/pure"
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['gravatar', 'series', 'sitemap', 'related_posts', 'neighbors',
           'liquid_tags.img', 'liquid_tags.video', 'liquid_tags.youtube',
           'liquid_tags.vimeo', 'liquid_tags.include_code',
           'pelican_gist', 'share_post']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)


# Social widget
SOCIAL = (('github', 'https://github.com/LucaLanziani'),
          ('twitter', 'http://twitter.com/lucalanziani'),
          ('linkedin', 'http://uk.linkedin.com/in/lucalanziani/'),
          ('envelope', 'mailto:luca.lanziani+site@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

PROFILE_IMG_URL = SITEURL + '/images/minime.jpg'
COVER_IMG_URL = SITEURL + '/images/london.jpg'
USER_LOGO_URL = SITEURL + '/images/minime.jpg'

TAGLINE = ('Software engineer, linux addict, '
           'hacker as http://bit.ly/hacker_def, '
           'InnovAction Lab alumnus')

TAGLINE_HTML = (
  'Software engineer, GNU/Linux addict, '
  '<a href="http://www.innovactionlab.org/"><i class="fa fa-link"></i></a>'
  'InnovAction Lab alumnus')

MENUITEMS = (('About', ''),
             ('Experience', 'pages/experience.html'),
             ('Blog', 'blog/'))


STATIC_PATHS = ['data', 'extra/CNAME', 'extra/favicon.ico'] + DEFAULT_CONFIG['STATIC_PATHS']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
