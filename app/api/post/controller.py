from flask import jsonify, request, current_app

from . import post
from .model import Post

@post.route('/', methods=['GET'])
def get_post():

    return jsonify({ "post": "sample post" })

