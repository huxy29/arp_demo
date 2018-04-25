#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: views.py
Author: <your-name> (<your-email>)
Date: 2018-03-12 17:21
Desc: 文章列表页面视图 
"""

from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request

from . import article_bp
from ..models import Article


@article_bp.route('/feed')
def feed():
    return 'This is article feed page'


@article_bp.route('/<id>')
def article(id):
    return 'This is article id-{} detail page'.format(id)
