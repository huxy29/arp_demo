#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: test_user_model.py
Author: %huxiaoyang% (%huxy29@outlook.com%)
Date: 2018-03-05 11:09
Desc:  
"""

import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, '../../')))
import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User()
        u.password='cat'
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User()
        u.password='cat'
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User()
        u.password='cat'
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User()
        u.password='cat'
        u2 = User()
        u2.password='cat'
        self.assertTrue(u.password_hash != u2.password_hash)


if __name__ == '__main__':
    unittest.main()
