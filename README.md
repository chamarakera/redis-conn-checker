# redis-conn-checker
A tool to continuously check connectivity to ElastiCache Redis

This tool can be used to check Elasticache Redis connectivity during following scenarios:
- ElastiCache Redis Cluster Engine Version Upgrades
- ElastiCache Redis Node Upgrades
- ElastiCache Redis Failover Testing

```sh
$ poetry install
$ poetry run python src/redis-conn-checker <primary_redis_endpoint> <primary_node_name>
```
