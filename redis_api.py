import redis
import json

def push(table):
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r.lpush('table', str(table))

def pop():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    data = json.loads(r.lpop('data'))

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