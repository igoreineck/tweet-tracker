from datetime import datetime
from flask import Blueprint, render_template, jsonify, request
from app.constants.redis import RedisConstants
from app.services.twitter import TwitterService
from app.services.redis import RedisService
from urllib import parse

import json
import os
import tweepy


messages = Blueprint(
    'messages',
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

def prepare_params(params: str):
    return params.replace(' ', ' OR ')

def encode_query(query: str):
    return parse.quote(query)

@messages.route('/messages', methods=['POST'])
def receive_hashtag():
    data = request.get_json()

    hashtags = data.get('hashtags')
    query = prepare_params(hashtags)
    query = encode_query(query)

    redis = RedisService()
    redis.set_param(RedisConstants.HASHTAGS.value, query)

    results = []

    try:
        tweepy_call = tweepy.Cursor(
            api.search,
            q=query,
            lang='pt',
            tweet_mode='extended'
        ).items(30)
    except tweepy.error.TempError as err:
        print("It was not possible to stabilish a connection")
    except Exception:
        import traceback
        traceback.print_exc()

    # for result in tweepy_call:
    #     item = result._json
    #     results.append({
    #         'created_at': item['created_at'],
    #         'message': item['full_text'],
    #         'user_name': item['user']['name'],
    #         'user_screen_name': item['user']['screen_name'],
    #         'user_profile_image': item['user']['profile_image_url_https']
    #     })

    teste = redis.get_param(RedisConstants.HASHTAGS.value)
    return jsonify(success=True, data=results)