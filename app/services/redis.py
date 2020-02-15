from app.constants.redis import RedisConstants
import os
import redis


class RedisService(object):
    def __init__(self):
        self._connection = redis.Redis(
            host=os.getenv('REDIS_HOST'),
            port=os.getenv('REDIS_PORT'),
            db=os.getenv('REDIS_DB'),
            charset='utf-8',
            decode_responses=True
        )
        self._QUEUE_START_POSITION = 0
        self._QUEUE_END_POSITION = -1
        self._QUEUE_INDEX_AMOUNT = 1
        self._session = self._connect()

    def _connect(self):
        return self._connection

    @property
    def get_queue(self):
        return self._session.lrange(RedisConstants.HASHTAGS.value,
            self._QUEUE_START_POSITION, self._QUEUE_END_POSITION)

    def enqueue(self, value: str):
        self._session.rpush(RedisConstants.HASHTAGS.value, value)

    def dequeue(self, value: str):
        return self._session.lrem(RedisConstants.HASHTAGS.value,
            self._QUEUE_INDEX_AMOUNT, value)