from app.services.redis import RedisService
from app.services.twitter import TwitterService
from flask import Blueprint, jsonify, request
from urllib import parse
from datetime import datetime
import dateutil.parser
import os
import requests
import tweepy


message_retrieve = Blueprint(
    'message_retrieve',
    __name__,
    template_folder='templates'
)

def join_params(params):
    if isinstance(params, bytes):
        return ' '.join(params.decode('utf-8'))
    return ' '.join(params)

def prepare_params(params):
    return params.replace(' ', ' OR ')

def encode_query(query):
    return parse.quote(query)


@message_retrieve.route('/message/retrieve', methods=['GET'])
def retrieve():
    redis = RedisService()
    service = TwitterService()

    service.authenticate()
    api = service.search()

    hashtags = redis.get_queue
    joined = join_params(hashtags)
    parsed = prepare_params(joined)
    query = encode_query(parsed)

    results = []
    success = False
    reason = ''

    if (bool(hashtags)):
        try:
            tweepy_call = service.cursor(api, q=query, lang='pt',
                tweet_mode='extended')

            for result in tweepy_call:
                item = result._json
                created_at = dateutil.parser.parse(item['created_at'])
                results.append({
                    'created_at': datetime.strftime(created_at, '%Y-%m-%d %H:%M:%S'),
                    'message': item['full_text'],
                    'user_name': item['user']['name'],
                    'user_screen_name': item['user']['screen_name'],
                    'user_profile_image': item['user']['profile_image_url_https']
                })
            success = True
        except tweepy.error.TweepError:
            reason = "It was not possible stabilish a connection"
        except Exception as exc:
            import traceback
            traceback.print_exc()
            reason = exc
    else:
        success = True
        reason = 'No hashtags to search'

    return jsonify(success=success, reason=reason, data=results)