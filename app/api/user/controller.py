from flask import jsonify, request, current_app

from . import user
from .model import User

@user.route('/', methods=['GET'])
def get_users():
    user_all = User.query.all();
    users = []
    for user in user_all:
        users.append({'name': user.name})

    return jsonify({'users': users})

