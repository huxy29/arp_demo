#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: forms.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-07 13:11
Desc:  
"""

from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField
from flask_wtf.file import FileRequired
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename

from .. import videos


class VideoForm(FlaskForm):
    """
    上传视频表单
    """
    upload = FileField(u'选择文件', validators=[
        FileRequired(),
        FileAllowed(['mp4'], u'支持 .mp4 文件上传')])
    submit = SubmitField(u'上传')
