#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: forms.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 15:40
Desc:  
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import Regexp
from wtforms.validators import EqualTo
from ..models import User
from wtforms import ValidationError


user_name_validators = [
    DataRequired(u'用户名不能为空'),
    Length(1, 64, u'1~64个字符'),
    Regexp('^[A-Za-z][A-Za-z0-9_]*$', 0, 
        u'用户名必须以字母开头，由字母、数字、下划线组成')
]
email_validators = [
    DataRequired(u'邮箱不能为空'),
    Length(1, 64, u'1~64个字符'),
    Email(u'请输入正确的邮箱')
]
password_validators = [
    DataRequired(u'密码不能为空'),
    Length(8, 100, u'至少8个字符'),
    Regexp('^[A-Za-z0-9@`~!@#$%^&*]*$', 0,
        u'密码由大小写字母、数字、及特殊字符`~!@#$%^&*组成')
]
password2_validators = [
    DataRequired(u'密码不能为空'),
    EqualTo('password', message=u'密码不一致，请重新输入')
]


class LoginForm(FlaskForm):
    """
    用户登录表单
    """
    user_name = StringField(u'用户名', validators=user_name_validators)
    password = PasswordField(u'密码', validators=password_validators)
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登录')


class RegistrationForm(FlaskForm):
    """
    用户注册表单
    """
    username = StringField(u'用户名', validators=user_name_validators)
    #email = StringField(u'邮箱', validators=email_validators)
    password = PasswordField(u'密码', validators=password_validators)
    password2 = PasswordField(u'确认密码', validators=password2_validators)
    submit = SubmitField(u'注册')

#    def validate_username(self, field):
#        if User.objects(username=field.data).first():
#            raise ValidationError(u'用户名已注册')

#    def validate_email(self, field):
#        if User.objects(User.email==field.data).first():
#            raise ValidationError(u'邮箱已注册')
#
#    def validate_username(self, field):
#        if User.objects(User.username==field.data).first():
#            raise ValidationError(u'用户名已被占用')

