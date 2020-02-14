import os
import tweepy


class TwitterService(object):

    def __init__(self):
        self._service = tweepy
        self._auth = None
        self._keys = {
            'consumer_key': str(os.getenv('CONSUMER_KEY')),
            'consumery_key_secret': str(os.getenv('CONSUMER_KEY_SECRET')),
            'access_token': str(os.getenv('ACCESS_TOKEN')),
            'access_token_secret': str(os.getenv('ACCESS_TOKEN_SECRET'))
        }

    def authenticate(self):
        self._auth = self._service.OAuthHandler(
            self._keys.get('consumer_key'),
            self._keys.get('consumer_key_secret')
        )
        self._auth.set_access_token(
            self._keys.get('access_token'),
            self._keys.get('access_token_secret')
        )
        return self._service

    @property
    def search(self):
        return self._service.API(self._auth).search

    def cursor(self, query, quantity=10, **params):
        return self._service.Cursor(query, **params).items(quantity)