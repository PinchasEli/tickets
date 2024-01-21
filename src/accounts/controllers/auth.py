# app/controllers/auth_controller.py
import jwt
import datetime
import os

from flask import request, jsonify

from ..models import Account


class AuthController:

    def login(self):
        try:
            data = request.get_json()

            if not data or 'username' not in data or 'password' not in data:
                raise 'Invalid request'

            username = data['username']
            password = data['password']

            user = Account.query.filter_by(username=username, password=password).first()
            # return user
            # user = AuthService.login(username, password)

            if not user:
                raise 'Invalid credentials'

            # Generate a token
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
            }, os.getenv("SECRET_KEY"), algorithm='HS256')

            # Return the token along with user information
            return jsonify({'message': 'Login successful', 'token': token, 'user': {'id': user.id, 'username': user.username}})
        except Exception as e:
            return jsonify({'error': f'Login account wrong: {e}'}), 400
