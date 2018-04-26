#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
File: api.py
Author: <your-name> (<your-email>)
Date: 2018-04-26 18:46
Desc:  
"""
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        # 获取前端传来的数据
        username = request.values.get('username')
        password = request.values.get('password')

        # 后端处理
        print username
        print password

        # 返回数据给前端
        res_json_obj = {
            'code': 0,
            'msg': 'test',
            'data': {
                'message': 'success'
            }
        }
        return jsonify(res_json_obj)


if __name__ == '__main__':
    app.run()

