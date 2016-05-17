#!/bin/sh

redis-cli -p 6379 SHUTDOWN
redis-cli -p 6380 SHUTDOWN
redis-cli -p 6381 SHUTDOWN
redis-cli -p 6382 SHUTDOWN
redis-cli -p 6383 SHUTDOWN

/bin/sh ~/www/culturalfes/culfes/redis.sh
