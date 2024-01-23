import sys
import socket
from loguru import logger


class Actions:
    def __init__(self, redis_connection, redis_endpoint) -> None:
        self.redis_connection = redis_connection
        self.redis_endpoint = redis_endpoint
        self.dummy_key = "foo"
        self.dummy_val = "bar"

    def write_to_db(self):
        """write dummy entry to redis endpoint DB"""
        try:
            result = self.redis_connection.set(self.dummy_key, self.dummy_val)
        except:
            result = sys.exc_info()[0]
        return result

    def read_from_db(self):
        """read dummy entry from redis endpoint DB"""
        try:
            result = self.redis_connection.get(self.dummy_key)
        except:
            result = sys.exc_info()[0]
        return result

    def delete_from_db(self):
        """deletes dummy entry from redis DB"""
        try:
            self.redis_connection.delete(self.dummy_key)
        except:
            logger.error(sys.exc_info()[0])

    def endpoint_lookup(self):
        """runs a DNS lookup to find the IP address of the redis endpoint"""
        return socket.getaddrinfo(self.redis_endpoint, 0, 0, 0, 0)[0][-1][0]
