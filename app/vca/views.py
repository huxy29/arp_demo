#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: views.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-06 15:21
Desc:  
"""

import os
import hashlib
from datetime import datetime
from flask import flash
from flask import url_for
from flask import send_from_directory
from flask import render_template
from flask import redirect
from flask import request
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import vca
from .. import videos
from .forms import VideoForm


UPLOAD_FILES_DIR = os.path.abspath(os.path.join(__file__, 
                                                '../../static/upload_files'))


def gen_md5(string):
    m = md5.new()
    m.update(string)
    return m.hexdigest()


def get_datetime():
    return datetime.now().strftime('%Y%m%d%H%M%S')


@vca.route('/', methods=['GET', 'POST'])
def entry_page():
    form = VideoForm()
    if form.validate_on_submit():
        f = form.upload.data
        filename = secure_filename(f.filename)
        filename = get_datetime() + filename 
        if not os.path.exists(UPLOAD_FILES_DIR):
            os.mkdir(UPLOAD_FILES_DIR)
        f.save(os.path.join(
            UPLOAD_FILES_DIR, filename 
        ))
        flash(u'上传成功')
        # 只能传递重定向的视图函数可以接受的参数
        return redirect(url_for('vca.result_page', fileid=filename))
    return render_template('vca/entry_page.html', form=form)


@vca.route('/result/<fileid>')
def result_page(fileid):
    if fileid:
        article = {
            "title": u"这是标题",
            "content": [
                {"image": "https://mdn.mozillademos.org/files/12371/newspaper_small.jpg"},
                {"text": u"https://mdn.mozillademos.org/files/12371/newspaper_small.jpg"}
            ]
        }
        url = url_for('static', filename='upload_files/{}'.format(fileid))
        return render_template('vca/result_page.html', url=url, article=article)
    return redirect(url_for('vca.entry_page'))
