#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: config.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-04 21:58
Desc: 参数配置
    <PARAM_KEY> = os.getenv('<PARAM_KEY>') or '<param_value>'
"""

import os

BASE_DIR = os.path.abspath(os.path.join(__file__, '../'))


class Config:
    """
    基础配置
    """
    SECRET_KEY = os.getenv('SECRET_KEY') or '1234567'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': os.getenv('DEV_DATABASE_NAME')
    }
    UPLOADS_DEFAULT_DEST = os.path.join(BASE_DIR, "upload_files")
    UPLOADS_DEFAULT_URL = "http://localhost:5000/"


class TestingConfig(Config):
    """
    测试环境配置
    """
    TESTING = True
    MONGODB_DATABASE_NAME = os.environ.get('TEST_DATABASE_NAME')



class ProductionConfig(Config):
    """
    生产环境配置
    """
    MONGODB_DATABASE_NAME = os.environ.get('DATABASE_NAME')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'productioin': ProductionConfig,

    'default': DevelopmentConfig
}

