# A dictionary: items -> key value pairs
dictionary = {}

# Creating dict from a list of keys
perms = ["read", "write", "modify"]
default_perms = dict.fromkeys(perms, False)
print(default_perms)

config = {
    "resolution": "1280x720",
    "fullscreen": True,
    "cpu": "intel i9 9900k"
}

config_2 = {
    "resolution": "1920x1080",
    "fullscreen": False,
    "cpu": "amd 64 x2"
}

# Acessing element using dict['key']
if "brightness" not in config:
    print("Brighntness key is missing")
else:
    print(f"Brightness is {config['brightness']}")

# Accessing element using dict.get('key', default value)
print(config.get('brightness', 100))

# Applying default value with dict.setdefault
config.setdefault("cpu", "Ryzen 5 5600X")
config["mouse"] = "logitech superlight"

# Update a dictionary with another dictionary (updates values and add values from new dictionary)
# config.update(config_2)

config |= config_2
# Same as config |= config_2

# Merge two dicts 
new_dict = config | config_2
print(config)