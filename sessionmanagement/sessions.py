import redis
import uuid

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

print(redis_db.keys())
#redis_db.set('012301223', str(uuid.uuid4()))
print(redis_db.keys())
b = redis_db.get('012301223')
if b:
    print("it's there")
    print(b.decode('utf-8'))
else:
    print("not there fam")

    #create redit object and methods
