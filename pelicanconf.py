#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
from pelican.settings import DEFAULT_CONFIG

AUTHOR = u'Luca Lanziani'
SITENAME = u'Luca Lanziani'
SITEURL = 'http://127.0.0.1:8000'

PATH = 'content'


TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'en'

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

DEFAULT_PAGINATION = 3
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

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

#
# Move content around
# All the blog related contents are created inside blog/ subdirectory
# the pages are outside the blog subfolder inside the pages/ directory
#

BLOG_PREFIX = 'blog/'

module = sys.modules[__name__]
# ENTITIES_SETTING
for entity in ['tag', 'category', 'author', 'article', 'draft']:
    url_key = "%s_URL" % entity.upper()
    save_as_key = "%s_SAVE_AS" % entity.upper()
    setattr(module, url_key, BLOG_PREFIX + DEFAULT_CONFIG[url_key])
    setattr(module, save_as_key, BLOG_PREFIX + DEFAULT_CONFIG[save_as_key])

# DIRECT_TEMPLATES_SETTING
for direct_template in DEFAULT_CONFIG['DIRECT_TEMPLATES']:
    save_as_key = "%s_SAVE_AS" % direct_template.upper()
    setattr(module, save_as_key, BLOG_PREFIX + '%s.html' % direct_template)
