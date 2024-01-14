# middlewares/api_middleware.py
from flask import Flask, jsonify, request

def api_response_middleware(response):
    # Check if the request is targeting an API route
    # if request.path.startswith('/api'):
    if response.status_code == 200:
        response.data = jsonify(status='success', data=response.get_json()).get_data()
    else:
        response.data = jsonify(status='error', error_message=response.get_json().get('error')).get_data()

    response.headers['X-API-Middleware'] = 'Response from API middleware!'

    return response

def init_app(app: Flask):
    app.after_request(api_response_middleware)
