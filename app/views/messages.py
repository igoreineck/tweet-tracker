from app.constants.redis import RedisConstants
from app.services.redis import RedisService
from flask import Blueprint, jsonify, request
from urllib import parse
import os
import requests
import tweepy


message_retrieve = Blueprint(
    'message_retrieve',
    __name__,
    template_folder='templates'
)

service = tweepy.OAuthHandler(
    os.getenv('CONSUMER_KEY'),
    os.getenv('CONSUMER_KEY_SECRET')
)
service.set_access_token(
    os.getenv('ACCESS_TOKEN'),
    os.getenv('ACCESS_TOKEN_SECRET')
)

api = tweepy.API(service)

redis = RedisService()
session = redis.connect()

def join_params(params: list):
    return ' '.join(params)

def prepare_params(params: str):
    return params.replace(' ', ' OR ')

def encode_query(query: str):
    return parse.quote(query)

@message_retrieve.route('/message/retrieve', methods=['GET'])
def retrieve():
    _ITEMS = 15

    hashtags = session.lrange(RedisConstants.HASHTAGS.value, 0, -1)
    joined = join_params(hashtags)
    parsed = prepare_params(joined)
    query = encode_query(parsed)

    results = []
    success = False
    reason = ''

    try:
        tweepy_call = tweepy.Cursor(
            api.search,
            q=query,
            lang='pt',
            tweet_mode='extended'
        ).items(_ITEMS)

        success = True
    except tweepy.error.TempError:
        reason = "It was not possible to stabilish a connection"
    except Exception as exc:
        import traceback
        traceback.print_exc()
        reason = exc

    for result in tweepy_call:
        item = result._json
        results.append({
            'created_at': item['created_at'],
            'message': item['full_text'],
            'user_name': item['user']['name'],
            'user_screen_name': item['user']['screen_name'],
            'user_profile_image': item['user']['profile_image_url_https']
        })
    return jsonify(success=True, data=results)