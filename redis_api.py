import redis
import json
import collections

def push(table):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.lpush('table', json.dumps(str(list(collections.Counter([(i[0]['id'], i[1]['id']) for i in table]).items()))))

def pop():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    data = r.lpop('data')
    if data==None:
        raise RuntimeError("No data in Redis")
    data = json.loads(data)

    users = []
    drivers = []
    max_distance = int(data["config"]["far_distance"])/30000
    type = data["config"]["type"]

    for order in data['user_list']:
        for user in range(int(order["size"])):
            users.append({
                "id": int(order["id"]),
                "coordinate": [float(i) for i in order["coordinate"]]
            })
    for driver in data['driver_list']:
        drivers.append({
            "id": int(driver["driver_id"]),
            "coordinate": [float(i) for i in driver["coordinate"]],
            "sites": int(driver["sites"])
        })
    return users, drivers, max_distance, type