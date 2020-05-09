import redis

myHostname = "MundoGlobo.redis.cache.windows.net"
myPassword = "N0JSNxNjAabXHfm2iKJqF6nQPYE++P2FnLZkfQWflU0="

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True, db=0)

result = r.ping()
print("Ping returned : " + str(result))

result = r.hset('100', 'nome', 'julio')
print("SET Message returned : " + str(result))

result = r.hset('100', 'email', 'julio@mundoglobo.com')
print("SET Message returned : " + str(result))

result = r.hgetall('100')
print(result)
#print("GET Message returned : " + result.decode("utf-8"))

# result = r.client_list()
# print("CLIENT LIST returned : ")
# for c in result:
#     print("id : " + c['id'] + ", addr : " + c['addr'])