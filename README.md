# redis-conn-checker
A tool to continuously check connectivity to ElastiCache Redis

This tool can be used to check Elasticache Redis connectivity during following scenarios:
- Cluster engine version upgrades
- ElastiCache Node upgrades
- Failover Testing

```sh
$ poetry install
$ poetry run python src/redis-conn-checker
```
