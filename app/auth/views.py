#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: views.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 13:12
Desc:  
"""

from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import request
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from . import auth
from ..models import User
from .forms import LoginForm
from .forms import RegistrationForm


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if User.objects(user_name=form.user_name.data).first():
            flash(u'该用户名已注册')
            return redirect(url_for('auth.register'))
        user = User()
        # 自增 id
        user_list = User.objects()
        if not user_list:
            user.user_id = '1'
        else:
            user_id_list = sorted([u.user_id for u in User.objects()])
            user.user_id = unicode(int(user_id_list[-1]) + 1)
        user.user_name = form.user_name.data
        user.password = form.password.data
        user.save()
        flash(u'注册成功，请登录')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(user_name=form.user_name.data).first()
        if user is None:
            flash(u'用户不存在')
        elif not user.verify_password(form.password.data):
            flash(u'密码错误')
        else:
            # 重要，真正地登录
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('home.entry'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已成功退出登录')
    return redirect(url_for('home.entry'))

