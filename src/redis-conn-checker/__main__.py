import sys

from actions import Actions
from connection import Connection
from loguru import logger
from validate import Validate


def usage():
    logger.info("Usage: poetry run python redis-conn-checker/src <primary_endpoint> <primary_node_name>")


def main():
    if len(sys.argv) > 1:
        redis_endpoint = sys.argv[1]
        redis_cluster_id = sys.argv[2]
    else:
        usage()
        sys.exit(1)

    redis_connection = Connection.conn(redis_endpoint)

    if redis_cluster_id in ["delete", "del"]:
        Actions(redis_connection, redis_endpoint).delete_from_db()
    else:
        Validate(redis_connection, redis_cluster_id, redis_endpoint).read_write_lookup()


if __name__ == "__main__":
    main()
