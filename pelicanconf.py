#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Isaac Zhou'
SITENAME = 'A Data Science Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# Themes
BS3_URL = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css'
BS3_JS  = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js'
BS3_THEME = 'https://bootswatch.com/default/bootstrap.min.css'

MENUITEMS = [
    ('Home', '/'),
    ('Posts By', [
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ('Tags', '/tags.html'),
        ]),
    ('Python', [
        ('Loop', '/loop.html'),
        ('Function', '/function.html'),
        ('Class', '/class.html'),
        ('List Comprehension', '/list-comprehension.html'),
        ]),
    ('Numpy', [
        ('Numpy Array', '/numpy-array.html'),
        ('Numpy Operation', '/numpy-operation.html'),
        ]),
    ('Pandas', [
        ('Pandas DataFrame', '/pandas-dataframe.html'),
        ('Pandas Read Data', '/pandas-read-data.html'),
        ('Pandas Data Cleaning', '/pandas-data-cleaning.html'),
        ('Pandas Data Manipulation', '/pandas-data-manipulation.html'),
        ('Pandas Data Analysis', '/pandas-data-analysis.html'),
        ('Pandas Data Visualization', '/pandas-data-visualization.html'),        
        ]),
    ('R', [
        ('Basics', '/r-basics.html'),
        ('Intermediate', '/r-intermediate.html'),
        ('Functions', '/r-functions.html'),
        ('Data Import', '/r-data-import.html'),
        ('Data Cleansing', '/r-data-cleansing.html'),
        ('dplyr', '/r-dplyr.html'),
        ('ggplot2', '/r-ggplot2.html'),
        ('Reporting', '/r-reporting.html'),
        ]),    
    ('SQL', [
        ('SELECT', '/SQL-select.html'),
        ('FILTER', '/SQL-filter.html'),
        ('SORT', '/SQL-sort.html'),
        ('GROUP', '/SQL-group.html'),
        ('JOIN', '/SQL-join.html'),
        ]),
    ('Machine Learning', [
        ('Linear Regression', '/linear-regression.html'),
        ('Logistic Regression', '/logistic-regression.html'),
        ('K Nearest Neighbors', '/knn.html'),
        ('Support Vector Machines', '/svm.html'),
        ('Principal Component Analysis', '/pca.html'),
        ('Recommender Systems', '/recommender-systems.html'),
        ('Natural Language Processing', '/nlp.html'),        
        ]),    
    ('Search', '000088558435892458427:1mn68z3f52e'),
    ]

FAVICON = u'https://photos-5.dropbox.com/t/2/AAApnB-1cvGXYPU5TzIpWjw2XO8gopGCMRMDpPUgANgneg/12/669394314/png/32x32/1/_/1/2/primerpyfavicon.png/EJzL47sFGI7MEyACKAI/ifTZBqf1Hxef7jG8ne_8la0vY3YzQTcFZUJL0Th_vi4?size=2048x1536&size_mode=3'

FAVICON_TYPE = u'png'
