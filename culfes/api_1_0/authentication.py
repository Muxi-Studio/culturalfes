# -*- coding: utf-8 -*-


from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from . import api
from ..models import User, AnonymousUser
from .errors import unauthorized, not_found, server_error


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    if email_or_token == '':
        g.current_user = AnonymousUser()
        return True

    if password == '':
        g.current_user = User.verify_auth_token(email_or_token)
        g.token_used = True
        return g.current_user is not None

    user = User.query.filter_by(email=email_or_token).first()
    if not user:
        return False

    g.current_user = user
    g.token_used = False

    return user.verify_password(password)


@api.before_request
def before_request():
    pass


@api.route('/token/', methods=['GET'])
@auth.login_required
def get_token():
    if isinstance(g.current_user, AnonymousUser) or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({
        'token': g.current_user.generate_auth_token()
        })


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


@auth.error_handler
def not_found_error():
    return not_found('Not found')


@auth.error_handler
def server_error_error():
    return server_error('Server error')
