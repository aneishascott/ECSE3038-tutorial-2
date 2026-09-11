readings = [
    {"name": "front-door", "room": "hall", "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def list_devices(devices):
    for device in devices:
        print(device["name"] + "," + str(device["temp"]))
list_devices(readings)

def average_temp(devices):
    total_temp = sum(device['temp'] for device in devices)
    return total_temp / len(devices) if devices else 0
print(f"Average Temperature: {average_temp(readings):.15f}")

def hottest_devices(devices):
    max_temp = devices[0]['temp']
    for i in range(len(devices)):
        if devices[i]['temp']>max_temp:
            max_temp = devices[i]['temp']
    hottest_device = next(device for device in devices if device['temp'] == max_temp)
    return hottest_device
print(hottest_devices(readings))

def to_status(device):
    return "Ok" if device['online'] else "Offline"
def device_status(devices):
    for device in devices:
        
        object_status = {"device" : device["name"],
                 "status" : to_status(device),
                 "celcius" : device["temp"]
                 } 
        if device['name'] == "fridge":
            print(object_status)
device_status(readings)

def by_room(devices):
    devices_by_room = {
        "hall": [],
        "attic": [],
        "kitchen": [],
        "outside": [],
    }
    for device in devices:
        room = device["room"]
        if room in devices_by_room:
            devices_by_room[room].append(device["name"])
    return devices_by_room

print(f"Devices by Room: {by_room(readings)}")