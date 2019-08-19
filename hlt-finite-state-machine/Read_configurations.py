import json

"""It returns the dictionary of configuration defined in config.json"""


def open_json():
    config_file_name = "config.json"
    with open(config_file_name) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config