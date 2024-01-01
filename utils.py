import yaml

class Config:
    def __init__(self, params):
        if params is not None:
            for key, value in params.items():
                if isinstance(value, dict):
                    setattr(self, key, Config(value))
                else:
                    setattr(self, key, value)


def read_params(config_path):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)
