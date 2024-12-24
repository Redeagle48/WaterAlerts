import toml
import json
import os

current_script_path = os.path.abspath(__file__)
current_script_dir = os.path.dirname(current_script_path)
parent_dir = os.path.dirname(current_script_dir)

# Read TOML file
config = toml.load(os.path.join(parent_dir, "config.toml"))

def get_mqtt_configs_as_json():
    mqtt_configs = {
        "mqtt_broker": config["mqtt"]["mqtt_broker"],
        "mqtt_port": config["mqtt"]["mqtt_port"],
        "mqtt_user": config["mqtt"]["mqtt_user"],
        "mqtt_password": config["mqtt"]["mqtt_password"]
    }
    return mqtt_configs#json.dumps(mqtt_configs, indent=4)

if __name__ == "__main__":
    # Access values
    db_host = config["mqtt"]["mqtt_broker"]
    db_port = config["mqtt"]["mqtt_port"]
    debug_mode = config["mqtt"]["mqtt_user"]

    print(f"Database host: {db_host}")
    print(f"Database port: {db_port}")
    print(f"Debug mode: {debug_mode}")