#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: __init__.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 01:33
Desc: 定义工厂函数，在工厂函数中通过注册蓝本的方式创建程序实例 
"""

from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_uploads import UploadSet
from flask_uploads import configure_uploads
from config import config


bootstrap = Bootstrap()
moment = Moment()
db = MongoEngine()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# 允许上传文件的类型
VIDEOS = tuple('mp4')
videos = UploadSet('videos', VIDEOS)


def create_app(config_name):
    """
    工厂函数
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    configure_uploads(app, (videos))

    from .home import home as home_blueprint
    from .auth import auth as auth_blueprint
    from .vca import vca as vca_blueprint
    from .article import article_bp
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(vca_blueprint, url_prefix='/vca')
    app.register_blueprint(article_bp, url_prefix='/article')

    return app

