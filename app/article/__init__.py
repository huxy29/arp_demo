#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: __init__.py
Author: <your-name> (<your-email>)
Date: 2018-03-12 17:09
Desc:  
"""

from flask import Blueprint

article_bp = Blueprint('articles', __name__)

from . import views
