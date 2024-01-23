import redis


class Connection:
    def __init__(self, redis_endpoint, port=6379, db=0, socket_timeout=1) -> None:
        self.port = port
        self.db = db
        self.socket_timeout = socket_timeout
        self.redis_endpoint = redis_endpoint

    def create(self):
        return redis.Redis(
            host=self.redis_endpoint,
            port=self.port,
            db=self.db,
            socket_timeout=self.socket_timeout,
        )
