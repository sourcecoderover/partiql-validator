import os
import yaml

from src import constants


def get_from_config_file() -> dict:
    config_path = os.path.join(resolve_resource_dir_path(), constants.CONFIG_FILE).replace("\\", "/")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def resolve_resource_dir_path():
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), constants.RESOURCES)
