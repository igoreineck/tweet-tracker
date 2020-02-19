from app.constants.redis import RedisConstants
import os
import redis


class RedisService(object):
    def __init__(self):
        self._host = os.getenv('REDIS_HOST') or 'localhost'
        self._port = os.getenv('REDIS_PORT') or 6379
        self._db = os.getenv('REDIS_DB') or 0
        self._charset = 'utf-8'
        self._decode_responses = True
        self._QUEUE_START_POSITION = 0
        self._QUEUE_END_POSITION = -1
        self._QUEUE_INDEX_AMOUNT = 1
        self._session = self._connect()

    def _connect(self):
        heroku_redis_connection = os.environ.get('REDIS_URL')
        if heroku_redis_connection:
            return redis.from_url(
                heroku_redis_connection,
                charset=self._charset,
                decode_responses=self._decode_responses
            )
        return redis.Redis(host=self._host, port=self._port, db=self._db,
            charset=self._charset, decode_responses=self._decode_responses)

    @property
    def get_queue(self):
        return self._session.lrange(RedisConstants.LISTNAME.value,
            self._QUEUE_START_POSITION, self._QUEUE_END_POSITION)

    def enqueue(self, value: str):
        self._session.rpush(RedisConstants.LISTNAME.value, value)

    def dequeue(self, value: str):
        return self._session.lrem(RedisConstants.LISTNAME.value,
            self._QUEUE_INDEX_AMOUNT, value)