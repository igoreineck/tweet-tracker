import os
import tweepy


class TwitterService(object):
    def __init__(self):
        self._ITEMS = 15
        self._keys = {
            'api_key': str(os.getenv('API_KEY')),
            'api_key_secret': str(os.getenv('API_KEY_SECRET')),
            'access_token': str(os.getenv('ACCESS_TOKEN')),
            'access_token_secret': str(os.getenv('ACCESS_TOKEN_SECRET'))
        }

    def authenticate(self):
        self._auth = tweepy.OAuthHandler(
            self._keys.get('api_key'),
            self._keys.get('api_key_secret')
        )
        self._auth.set_access_token(
            self._keys.get('access_token'),
            self._keys.get('access_token_secret')
        )

    def search(self):
        return tweepy.API(self._auth).search

    def cursor(self, *args, **params):
        return tweepy.Cursor(*args, **params)\
            .items(params.get('quantity', self._ITEMS))