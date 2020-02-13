from datetime import datetime
from flask import Blueprint, render_template, jsonify, request
from app.services.twitter import TwitterService
import json
import os
import tweepy


messages = Blueprint(
    'messages',
    __name__,
    template_folder='templates'
)

def format_hashtag(hashtag):
    return "#{}".format(hashtag)

@messages.route('/messages', methods=['POST'])
def receive_hashtag():
    data = request.get_json()
    param = format_hashtag(data['hashtag'])

    # TODO: transfer this call to the functools
    # TODO: use the service correctly later
    # service = TwitterService()
    # service.authenticate()
    # api = service.execute

    service = tweepy.OAuthHandler(
        os.getenv('CONSUMER_KEY'),
        os.getenv('CONSUMER_SECRET')
    )
    service.set_access_token(
        os.getenv('ACCESS_TOKEN'),
        os.getenv('ACCESS_TOKEN_SECRET')
    )
    api = tweepy.API(service)

    tweepy_call = tweepy.Cursor(
        api.search,
        q=param,
        lang='pt',
        tweet_mode='extended'
    ).items(20)

    results = []
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