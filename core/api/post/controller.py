from flask import Blueprint, jsonify, request, current_app

from core.api.post.model import Post

post = Blueprint('post', __name__)

@post.route('/', methods=['GET'])
def get_post():

    return jsonify({ "post": "sample post" })

