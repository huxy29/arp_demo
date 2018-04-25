#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: __init__.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 13:10
Desc:  
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
