#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: models.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 09:56
Desc:  
"""

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import LoginManager
from flask_login import UserMixin
from . import db
from . import login_manager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


class User(UserMixin, db.Document):
    
    meta = {
        'collection': 'users',
        'ordering': ['-create_at'],
        'strict': False,
    }
    user_id = db.StringField(primary_key=True, required=True)
    user_name = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)
    password_hash = db.StringField(required=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.objects().get_or_404(user_id=user_id)


class Article(db.Document):

    meta = {
        'collection': 'articles',
        'ordering': ['-create_at'],
        'strict': False
    }
    id = db.StringField(primary_key=True, required=True)
    title = db.StringField(unique=True, required=True)
    
