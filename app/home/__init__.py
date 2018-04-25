#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: __init__.py
Author: huxy29
Date: 2018-03-05 01:38
Desc:  
"""

from flask import Blueprint

home = Blueprint('home', __name__)

from . import views

