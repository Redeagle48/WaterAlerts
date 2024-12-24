import myscrape
import openai_client
import store_scrappingValue
import MQTT_client
import json
import logging
import sys
from datetime import datetime

logging.basicConfig(level=logging.INFO)

MQTT_TOPIC = 'roturas/text'

if __name__ == "__main__":
    logging.info(f"Running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")

    try:
        text = myscrape.scrape_roturas()
        if text is None:
            logging.error("Failed to scrape text.")
            logging.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")
            sys.exit(1)
        
        isNewValue = store_scrappingValue.processValue(text)
        if not isNewValue:
            logging.info("No new value found. Exiting.")
            logging.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")
            sys.exit(0)
        
        processedValue_json = openai_client.generate_water_outage_info(text)

        if processedValue_json is not None:
            if processedValue_json['HasWaterOutage']:
                MQTT_client.publish_to_mqtt(MQTT_TOPIC, json.dumps(processedValue_json))
            else:
                processedValue_json['message'] = "No water outage"
                MQTT_client.publish_to_mqtt(MQTT_TOPIC, json.dumps(processedValue_json))
        else:
            logging.error("Error: processedValue_json is None")
            logging.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")
            sys.exit(1)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        logging.info(f"Finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =================")
        sys.exit(1)