import json

"""
Module used to read the configuration file in json format
"""


def open_json(conf):
    with open(conf) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config

