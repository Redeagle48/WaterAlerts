import myscrape
import openai_client
import store_scrappingValue
import MQTT_client
import json
import logging
import sys
from datetime import datetime
import configurations_processor as configs

logging.basicConfig(level=logging.INFO)

def log_and_exit(message, level="info", exit_code=0):
    log_message = f"{message} Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ================="
    if level == "error":
        logging.error(log_message)
    else:
        logging.info(log_message)
    sys.exit(exit_code)

if __name__ == "__main__":
    logging.info(f"Running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")

    try:
        text = myscrape.scrape_roturas()
        if not text:
            log_and_exit("Failed to scrape text.", level="error", exit_code=1)
     
        isNewValue = store_scrappingValue.processValue(text)
        if not isNewValue:
            log_and_exit("No new value found. Exiting.", exit_code=0)
        
        processedValue_json = openai_client.generate_water_outage_info(text)

        if processedValue_json is not None:
            MQTT_TOPIC = configs.get_mqtt_configs_as_json()["topic"]
            if processedValue_json['HasWaterOutage']:
                MQTT_client.publish_to_mqtt(MQTT_TOPIC, json.dumps(processedValue_json))
            else:
                processedValue_json['message'] = "No water outage"
                MQTT_client.publish_to_mqtt(MQTT_TOPIC, json.dumps(processedValue_json))
            
            log_and_exit("Process completed successfully.", exit_code=0)

        else:
            log_and_exit("Error: processedValue_json is None", level="error", exit_code=1)

    except Exception as e:
        log_and_exit(f"An error occurred: {e}", level="error", exit_code=1)