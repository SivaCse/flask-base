import json
from flask import Blueprint, jsonify, request, current_app, Response

from core.api.user.model import User

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():
    user_all = User.query.all();
    users = []
    for user in user_all:
        users.append({'name': user.name})

    return jsonify({'users': users})

