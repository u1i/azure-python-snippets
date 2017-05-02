#!/home/uli/azure/redis/bin/python
# Redis performance test - run with the following command on the shell:
# time python redis_testing.py
import redis, string, random

def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# Assuming you have a local Redis cache as well
redis_localhost = redis.Redis(
    host = '127.0.0.1',
    port = 6379, 
    password = '')

redis_azure = redis.Redis(
    host = 'YOUR_CACHE.redis.cache.windows.net',
    port = 6379, 
    password = 'ACCESS_KEY')

r = redis_azure

# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)

for run in range(1,1000000):
	key = "sdx_"+id_generator()
	val = random.randint(1,999999999)

	r.set(key, val)
	# print key + " -> " + str(val)

