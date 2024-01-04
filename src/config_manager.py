import json


class ConfigManager:
    def __init__(self, config_location="./config.json"):
        self.config_location = config_location
        file = open(config_location, "r")
        self.config = json.load(file)

    def get(self, key: str):
        return self.config[key]
