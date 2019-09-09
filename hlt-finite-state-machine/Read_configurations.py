import json

"""It returns the dictionary of configuration defined in config.json"""


def open_json(file_name):
    with open(file_name) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config