import paho.mqtt.client as mqtt
import logging
import configurations_processor as configs

# Configure logging
logging.basicConfig(level=logging.INFO)

# MQTT broker connection details
mqtt_configs = configs.get_mqtt_configs_as_json()

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        logging.info("Connected to MQTT Broker!")
    else:
        logging.error(f"Failed to connect, return code {rc}")

def publish_to_mqtt(topic, message):

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.username_pw_set(mqtt_configs["mqtt_user"], mqtt_configs["mqtt_password"])
    client.on_connect = on_connect

    try:
        client.connect(mqtt_configs["mqtt_broker"], mqtt_configs["mqtt_port"], 60)
        client.loop_start()
        #result = client.publish(topic, message)
        #status = result.rc
        #if status == mqtt.MQTT_ERR_SUCCESS:
        #    logging.info(f"Sent `{message}` to topic `{topic}`")
        #else:
        #    logging.error(f"Failed to send message to topic {topic}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    # Example usage
    example_topic = "test/topic"
    example_message = "Hello, MQTT!"
    publish_to_mqtt(example_topic, example_message)