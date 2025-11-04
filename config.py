import os.path
import yaml


class Config:
    CONFIG_PATH = os.path.join(os.getcwd(), "config.yaml")

    def __init__(self):
        self.load_config()

    def load_config(self):
        if os.path.exists(self.CONFIG_PATH):
            with open(self.CONFIG_PATH) as file:
                self.data = yaml.full_load(file.read())
        else:
            raise FileNotFoundError("Config not found")

    def save_config(self, file):
        yaml.dump(self.data, default_flow_style=False)

    def __getattr__(self, key):
        # Use __getattr__ instead of __getattribute__ for fallback behavior
        if key in self.data:
            return self.data[key]
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")
