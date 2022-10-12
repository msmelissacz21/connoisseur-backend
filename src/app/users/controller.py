from flask import Blueprint, request
from .repository import get_user_by_id, save
from base64 import b64decode
from ast import literal_eval
import json

users = Blueprint('auth', __name__)

@users.route('/sign-in-or-sign-up', methods = ['GET'])
def get_recipe():

    user = get_user_by_id('test')
    if not user:
        token = request.args.get('access_token')
        payload = get_token_payload(token)

        user_record = {
            'user_id': payload['username'],
            'recipe_ids': []
        }
        save(user_record)

        user = user_record

    return json.dumps(user), 200, {'Access-Control-Allow-Origin': '*'}


# in the future should verify token first
def get_token_payload(token: str) -> dict:
    payload = token.split('.')[1]
    return literal_eval(b64decode(payload+'==').decode('utf-8'))