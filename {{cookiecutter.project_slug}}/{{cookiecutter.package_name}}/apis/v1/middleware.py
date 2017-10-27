import json

from flask import current_app, request
from werkzeug.wrappers import Response
from werkzeug.exceptions import HTTPException


def check_auth(auth):
    un = current_app.config['BASIC_AUTH_USERNAME']
    pw = current_app.config['BASIC_AUTH_PASSWORD']
    return auth.username == un and auth.password == pw


def basic_auth(endpoint):

    auth = request.authorization
    if not auth or not check_auth(auth):
        resp = Response(
            response=json.dumps({'message': 'Not Authorized', 'error': True}),
            headers = {
                'WWW-Authenticate': 'Basic realm="Login Required"'
            },
            mimetype='application/json',
            status=401
        )
        raise HTTPException('Api Error', response=resp)
