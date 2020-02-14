import os
import redis

class RedisService(object):

    _connection = redis.StrictRedis(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        db=os.getenv('REDIS_DB'),
        charset='utf-8',
        decode_responses=True
    )

    @classmethod
    def get_param(cls, param: str):
        return cls._connection.get(param)

    @classmethod
    def set_param(cls, param: str, value):
        cls._connection.set(param, value)