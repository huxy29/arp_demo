#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: manage.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-04 21:58
Desc:  
"""

import os
from app import create_app
from app import db
from app.models import User
from flask_script import Manager
from flask_script import Shell
from flask_mongoengine import MongoEngine


app = create_app(os.getenv('FLASK_CONFIG_NAME') or 'default') 
manager = Manager(app)
db = MongoEngine(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
