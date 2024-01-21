# app/decorators/auth_decorators.py
import jwt
import os

from flask import request, jsonify

from functools import wraps

from ..accounts.models import Account

# Decorator to check if the request has a valid token and retrieve user information
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256'])
            current_account = Account.query.get(data['user_id'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(current_account, *args, **kwargs)

    return decorated
