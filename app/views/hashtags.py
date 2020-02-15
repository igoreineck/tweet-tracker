from app.constants.redis import RedisConstants
from app.services.redis import RedisService
from flask import Blueprint, render_template, jsonify, request

save = Blueprint('save', __name__, template_folder='templates')
retrieve = Blueprint('retrieve', __name__, template_folder='templates')

redis = RedisService()
session = redis.connect()


@save.route('/hashtag/save', methods=['POST'])
def receive_hashtags():
    data = request.get_json()
    hashtags = data.get('hashtags')

    for hashtag in hashtags.split():
        session.rpush(RedisConstants.HASHTAGS.value, hashtag)

    return jsonify(success=True)

@retrieve.route('/hashtag/retrieve', methods=['GET'])
def retrieve_hashtags():
    hashtags = session.lrange(RedisConstants.HASHTAGS.value, 0, -1)
    return jsonify(success=True, data=hashtags)