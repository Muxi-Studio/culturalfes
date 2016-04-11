# -*- coding: utf-8 -*-


from flask import jsonify
from . import api
from app.exceptions import ValidationError


def not_found(message):
    response = jsonify({'error': 'not_found', 'message': message})
    response.status_code = 404
    return response


def unauthorized(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
