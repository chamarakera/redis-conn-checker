import sys
import time

import boto3
import redis
from actions import Actions
from loguru import logger


class Validate:
    def __init__(
        self,
        redis_connection: redis.client.Redis,
        redis_cluster_id: str,
        redis_endpoint: str,
        region="us-west-2",
    ) -> None:
        self.redis_connection = redis_connection
        self.redis_cluster_id = redis_cluster_id
        self.redis_endpoint = redis_endpoint
        self.redis_client = boto3.client("elasticache", region_name=region)
        self.interval = 0.5

    def read_write_lookup(self) -> None:
        """Outputs cluster status, ability to read and write
        from Redis DB and Redis Node IP Address"""
        action = Actions(self.redis_connection, self.redis_endpoint)

        while True:
            try:
                response = self.redis_client.describe_cache_clusters(
                    CacheClusterId=self.redis_cluster_id,
                    ShowCacheNodeInfo=True,
                )
                logger.info(
                    f"Cluster Status: {response['CacheClusters'][0]['CacheClusterStatus']}, "
                    f"Write: {action.write()}, "
                    f"Read: {action.read()}, "
                    f"Node IP: {action.lookup()}"
                )
                time.sleep(self.interval)
            except KeyboardInterrupt:
                logger.warning("Exiting program...")
                sys.exist(1)
