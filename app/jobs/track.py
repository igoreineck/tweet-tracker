from app.services.redis import RedisService
from urllib import parse
import os
import requests
import tweepy


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


# TODO: improve these extractions

# query = prepare_params(hashtags)
# query = encode_query(query)

# results = []
# success = False
# reason = ''

# try:
#     tweepy_call = tweepy.Cursor(
#         api.search,
#         q=query,
#         lang='pt',
#         tweet_mode='extended'
#     ).items(30)

#     success = True
# except tweepy.error.TempError:
#     reason = "It was not possible to stabilish a connection"
# except Exception as exc:
#     import traceback
#     traceback.print_exc()
    # reason = exc

# for result in tweepy_call:
#     item = result._json
#     results.append({
#         'created_at': item['created_at'],
#         'message': item['full_text'],
#         'user_name': item['user']['name'],
#         'user_screen_name': item['user']['screen_name'],
#         'user_profile_image': item['user']['profile_image_url_https']
#     })


# class TrackTweets(object):

#     _REDIS = RedisService()

