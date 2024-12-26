import json
import os
import logging
from openai import OpenAI
import configurations_processor as configs

# Configure logging
logging.basicConfig(level=logging.INFO)
configs = configs.get_openai_configs_as_json();
API_KEY = configs["api_key"]
MODEL = configs["model"]

def generate_water_outage_info(newValue):
    """
    Generate water outage information using OpenAI's API.

    Args:
        newValue (str): The newly scraped text.

    Returns:
        dict: A dictionary containing the water outage information, or None if an error occurs.
    """
    if not API_KEY:
        logging.error("OpenAI API key is not set.")
        return None

    client = OpenAI(api_key=API_KEY)

    try:
        completion = client.chat.completions.create(
            model = MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant and will analyze a raw info about non programmed water issues."},
                {"role": "user", "content": "Check if I have or will have a water issue in Vila de Rei/Bucelas, Portugal. Return as answer a JSON structure with attribute 'HasWaterOutage' with value true/false where true means water issue in Vila de Rei or Bucelas, otherwise false. If true, an attribute 'Message' of type text with a text containing pertinent info and, if possible, when it starts and when ends."},
                {"role": "user", "content": newValue}
            ]
        )
        response_text = completion.choices[0].message.content

        # Extract the JSON content
        start = response_text.find('{')
        end = response_text.rfind('}') + 1
        response_json = response_text[start:end]

        try:
            response_json = json.loads(response_json)
            return response_json
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")
            return None

    except Exception as e:
        logging.error(f"An error occurred while calling the OpenAI API: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    example_text = "Example water outage information."
    result = generate_water_outage_info(example_text)
    if result:
        logging.info(f"Generated water outage info: {result}")
    else:
        logging.error("Failed to generate water outage info.")