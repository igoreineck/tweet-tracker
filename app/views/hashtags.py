from app.constants.redis import RedisConstants
from app.services.redis import RedisService
from flask import Blueprint, render_template, jsonify, request

hashtag_save = Blueprint(
    'hashtag_save',
    __name__,
    template_folder='templates'
)
hashtag_retrieve = Blueprint(
    'hashtag_retrieve',
    __name__,
    template_folder='templates'
)
hashtag_remove = Blueprint(
    'hashtag_remove',
    __name__,
    template_folder='templates'
)


@hashtag_save.route('/hashtag/save', methods=['POST'])
def receive():
    redis = RedisService()
    data = request.get_json()
    hashtags = data.get('hashtags')
    for hashtag in hashtags.split():
        redis.queue(hashtag)
    return jsonify(success=True)

@hashtag_retrieve.route('/hashtag/retrieve', methods=['GET'])
def retrieve():
    redis = RedisService()
    hashtags = redis.queue
    return jsonify(success=True, data=hashtags)

@hashtag_remove.route('/hashtag/remove', methods=['POST'])
def remove():
    data = request.get_json()
    hashtag = data.get('hashtag')
    return jsonify(success=True)