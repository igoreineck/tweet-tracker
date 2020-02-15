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

    def connect(self):
        return self._connection