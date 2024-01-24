import socket
from socket import gaierror

import redis
from loguru import logger


class Actions:
    def __init__(self, redis_connection: redis.client.Redis, redis_endpoint: str) -> None:
        self.redis_connection = redis_connection
        self.redis_endpoint = redis_endpoint
        self.dummy_key, self.dummy_val = "foo", "bar"

    def write(self) -> bool:
        """write dummy entry to redis endpoint DB"""
        try:
            return self.redis_connection.set(self.dummy_key, self.dummy_val)
        except redis.exceptions.RedisError:
            return False

    def read(self) -> str:
        """read dummy entry from redis endpoint DB"""
        try:
            return self.redis_connection.get(self.dummy_key)
        except redis.exceptions.RedisError as e:
            return e

    def delete(self) -> None:
        """deletes dummy entry from redis DB"""
        try:
            self.redis_connection.delete(self.dummy_key)
            logger.info(f"Dummy entry {self.dummy_val} deleted")
        except redis.exceptions.RedisError as e:
            logger.error(e)

    def lookup(self) -> str:
        """runs a DNS lookup to find the IP address of the redis endpoint"""
        try:
            return socket.getaddrinfo(self.redis_endpoint, 0, 0, 0, 0)[0][-1][0]
        except gaierror as e:
            return e
