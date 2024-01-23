import time
import boto3
from loguru import logger
from actions import Actions


class Validate:
    def __init__(
        self, redis_connection, redis_cluster_id, redis_endpoint, region
    ) -> None:
        self.redis_connection = redis_connection
        self.redis_cluster_id = redis_cluster_id
        self.redis_endpoint = redis_endpoint
        self.redis_client = boto3.client("elasticache", region_name=region)
        self.interval = 0.5

    def read_write(self):
        action = Actions(self.redis_connection)
        while True:
            response = self.redis_client.describe_cache_clusters(
                CacheClusterId=self.redis_cluster_id,
                ShowCacheNodeInfo=True,
            )
            logger.info(
                f"{response['CacheClusters'][0]['CacheClusterStatus']}"
                f"{action.write_to_db()}"
                f"{action.read_from_db()}"
                f"{action.endpoint_lookup}"
            )
            time.sleep(self.interval)
