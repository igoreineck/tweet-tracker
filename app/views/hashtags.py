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

redis = RedisService()
session = redis.connect()


@hashtag_save.route('/hashtag/save', methods=['POST'])
def receive():
    data = request.get_json()
    hashtags = data.get('hashtags')

    for hashtag in hashtags.split():
        session.rpush(RedisConstants.HASHTAGS.value, hashtag)

    return jsonify(success=True)

@hashtag_retrieve.route('/hashtag/retrieve', methods=['GET'])
def retrieve():
    hashtags = session.lrange(RedisConstants.HASHTAGS.value, 0, -1)
    return jsonify(success=True, data=hashtags)