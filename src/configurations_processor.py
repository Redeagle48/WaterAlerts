import toml
import json
import os

CONFIG_FILE = "config.toml"

current_script_path = os.path.abspath(__file__)
current_script_dir = os.path.dirname(current_script_path)
parent_dir = os.path.dirname(current_script_dir)

# Read TOML file
config = toml.load(os.path.join(parent_dir, CONFIG_FILE))

def get_configs(section=""):
    if section:
        return config.get(section)
    else:
        return config

def get_mqtt_configs_as_json():
    return get_configs("mqtt")

def get_openai_configs_as_json():
    return get_configs("openai")

def get_app_configs_as_json():
    return get_configs("application")

if __name__ == "__main__":

    out = get_configs("openai")
    out = out

    # Access values
    #db_host = config["mqtt"]["mqtt_broker"]
    #db_port = config["mqtt"]["mqtt_port"]
    #debug_mode = config["mqtt"]["mqtt_user"]

    #print(f"Database host: {db_host}")
    #print(f"Database port: {db_port}")
    #print(f"Debug mode: {debug_mode}")