from app.constants.redis import RedisConstants
from app.services.redis import RedisService
from flask import Blueprint, render_template, jsonify, request

save = Blueprint('save', __name__, template_folder='templates')
retrieve = Blueprint('retrieve', __name__, template_folder='templates')


@save.route('/save', methods=['POST'])
def receive_hashtags():
    data = request.get_json()
    hashtags = data.get('hashtags')

    redis = RedisService()
    redis.set_param(
        RedisConstants.HASHTAGS.value,
        str(hashtags.split())
    )

    teste = redis.get_param(RedisConstants.HASHTAGS.value)
    print("QUERY: ", teste)
    return jsonify(success=True)

@retrieve.route('/retrieve', methods=['GET'])
def retrieve_hashtags():
    redis = RedisService()
    hashtags = redis.get_param(RedisConstants.HASHTAGS.value)
    return jsonify(success=True, data=hashtags)