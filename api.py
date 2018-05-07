# -*- coding: utf-8 -*-

import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask_mongoengine import MongoEngine
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

# initialization
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/arp_demo',
    'connect': False
}
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

# extensions
db = MongoEngine(app)
auth = HTTPBasicAuth()


class User(db.Document):
    meta = {
        'collection': 'users',
        'ordering': ['-create_at'],
        'strict': False
    }
    id = db.StringField(primary_key=True, required=True)
    username = db.StringField(unique=True, required=True)
    password_hash = db.StringField(required=True)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.objects(id=data['id'])
        return user


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.objects(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@app.route('/arp/api/users', methods=['POST'])
def user_register():
    username = request.values.get('username')
    password = request.values.get('password')
    if username is None or password is None:
        return (
            jsonify({
                'error_code': 400,
                'message': 'missing username or password'
            }),
            400)
    if User.objects(username=username).first() is not None:
        return (
            jsonify({
                'error_code': 400,
                'message': 'username existing'
            }),
            400
        )
    user_list = User.objects()
    if not user_list:
        id = '1'
    else:
        id_list = sorted([u.id for u in User.objects()])
        id = unicode(int(id_list[-1]) + 1)
    user = User(id=id, username=username)
    user.hash_password(password)
    user.save()
    return (
        jsonify({'username': user.username}),
        201,
        {'Location': url_for('get_user', id=user.id, _external=True)}
    )


@app.route('/arp/api/users/login', methods=['POST'])
def user_login():
    username = request.values.get('username')
    password = request.values.get('password')
    user = User.objects(username=username).first()
    if not user:
        return jsonify({
            'error_code': 404,
            'message': 'username does not exist'
        })
    elif user.verify_password(password):
        return jsonify({
            'error_code': 200,
            'message': 'sucess'
        })
    else:
        return jsonify({
            'error_code': 404,
            'message': 'failure'
        })


@app.route('/api/users/<int:id>')
@auth.login_required
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})


if __name__ == '__main__':
    app.run(debug=True)