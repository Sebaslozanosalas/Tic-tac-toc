import json

class SettingsManager:
    def __init__(self):
        self.path = 'settings/config.json'


    def get_settings(self):
        with open(self.path, 'r') as f:
            config = json.load(f)
        return config
    
    