readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(device["name"] + " " + str(device["temp"]))
list_devices(readings)

def average_temp(devices):
    total_temp = sum(device['temp'] for device in devices)
    return total_temp / len(devices) if devices else 0
print(f"Average Temperature: {average_temp(readings):.15f}")

def hottest(devices):
    max_temp = devices[0]['temp']
    for i in range(len(devices)):
        if devices[i]['temp']>max_temp:
            max_temp = devices[i]['temp']
    hottest_device = next(device for device in devices if device['temp'] == max_temp)
    return hottest_device
print(hottest(readings))

def to_status(device):
    if device["online"] == True:
        status = "ok"
    else:
        status = "offline"
    result = {}
    result["device"] = device["name"]
    result["status"] = status  
    result["celsius"] = device["temp"]
    return result
print(to_status(readings[3]))

def by_room(devices):
    devices_by_room = {}
    for device in devices:
        room = device["room"]
        if room not in devices_by_room:
            devices_by_room[room] = []
        devices_by_room[room].append(device["name"])
    return devices_by_room

print(by_room(readings))