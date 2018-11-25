
from functools import wraps

import jwt
from flask import request, session

from errors import http_error
from utils import config

BEARER_PREFIX = 'Bearer'


def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        authHeader = request.headers.get('Authorization')
        bearer, _, token = authHeader.partition(' ')

        if bearer != BEARER_PREFIX:
            return unauthorized("Invalid authorization header")

        try:
            decoded_token = jwt.decode(
                token, config.JWT_AUTH['secret'], config.JWT_AUTH['algorithm'])
            session['id'] = decoded_token["userId"]

        except jwt.InvalidTokenError:
            return unauthorized("Invalid token")
        except jwt.ExpiredSignatureError:
            return unauthorized("Token has expired")

        return func(*args, **kwargs)

    return check_token


def unauthorized(message):
    return http_error.response(401, message)
