from redis_state import Redis_state
from limiter import Limiter
class ThrottlePy:
    def __init__(self):
        self.state = Redis_state("localhost", 6379)
        self.limiter = Limiter(self.state)

