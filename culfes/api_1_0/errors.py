# -*- coding: utf-8 -*-


from flask import jsonify
from . import api


def not_found(message):
    response = jsonify({'error': 'not_found', 'message': message})
    response.status_code = 404
    return response
