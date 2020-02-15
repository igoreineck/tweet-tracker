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
def save():
    redis = RedisService()
    data = request.get_json()
    hashtags = data.get('hashtags')
    for hashtag in hashtags.split():
        redis.enqueue(str(hashtag))
    return jsonify(success=True)

@hashtag_retrieve.route('/hashtag/retrieve')
def retrieve():
    redis = RedisService()
    hashtags = redis.get_queue
    return jsonify(success=True, data=hashtags)

@hashtag_remove.route('/hashtag/remove', methods=['POST'])
def remove():
    data = request.get_json()
    hashtag = data.get('hashtag')

    redis = RedisService()
    status = redis.dequeue(str(hashtag))

    success = False
    if status:
        success = True

    return jsonify(success=success)