import os
import tweepy


class TwitterService(object):

    def __init__(self):
        self._service = tweepy
        self._auth = None
        self._keys = dict(
            consumer_key=os.getenv('CONSUMER_KEY'),
            consumery_key_secret=os.getenv('CONSUMER_KEY_SECRET'),
            access_token=os.getenv('ACCESS_TOKEN'),
            access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
        )

    def authenticate(self):
        self._auth = self._service.OAuthHandler(
            self._keys.get('consumer_key'),
            self._keys.get('consumer_key_secret')
        )
        self._auth.set_access_token(
            self._keys.get('access_token'),
            self._keys.get('access_token_secret')
        )

    @property
    def execute(self):
        return self._service.API(self._auth)

    def cursor(self, query, **params):
        return self._service.Cursor(query, **params)