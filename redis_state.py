import redis

class Redis_state:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.redis_cli = redis.Redis(
            host=host,
            port=port,
            charset="utf-8",
            decode_responses=True
        )


    def _test_connection(self):
        if self.redis_cli.ping():
            print("Redis Connection Active")

    