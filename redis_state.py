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

    def set_to_state(self, name, value):
        is_stored = self.redis_cli.set(name, value);
        return is_stored
    def get_from_state(self, name):
        state_value = self.redis_cli.get(name);
        return state_value
    def check_in_state(self, name):
        is_in_state = self.redis_cli.get(name)
        if is_in_state:
            return True
        else:
            return False
    