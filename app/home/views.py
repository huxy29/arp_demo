#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: views.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 20:42
Desc:  
"""

from flask import render_template
from flask_login import login_required
from . import home
from .. import login_manager
from ..models import User


@home.route('/')
def entry():
    return render_template('home/entry.html')


@login_manager.user_loader
def load_user(user_id):
    return User.objects(user_id=user_id).first()
