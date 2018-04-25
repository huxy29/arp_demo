#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: __init__.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-06 15:16
Desc:  
"""

from flask import Blueprint

vca = Blueprint('vca', __name__)

from . import views
