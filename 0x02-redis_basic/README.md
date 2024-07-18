0x02. Redis basic
About
Redis basics
Redis for simple caching
Creating redis clients with redis-py library
Tasks
Writing string to Redis:

class Cache implementation
method store implementation
File: exercise.py
Reading from Redis and recovering original type using redis-py

Methods implementation: get_str and get_int
File: exercise.py
Incrementing values on Redis

Implementation of count calls function-based decorator for Cache.store method
File: exercise.py
Storing list elements in Redis

Implementation of call_history function-based decorator for Cache.store method.
File: exercise.py
Retrieving list elements from Redis

Implementation of replay function to display history of a particular function based on data retrieved from Redis
File: exercise.py
Implementing an expiring web cache and tracker

Function get_page for making requests and tracking url access count
File: web.py
