import requests
from bs4 import BeautifulSoup
import logging

SCRAPE_URL = "https://www.simar-louresodivelas.pt/index.php/roturas-com-texto"

logging.basicConfig(level=logging.INFO)

def scrape_roturas():
    """
    Scrape the water outage information from the specified URL.

    Returns:
        str: The scraped text content if successful, None otherwise.
    """
    url = SCRAPE_URL

    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content section based on specific styles
        content_div = soup.find("div", style=lambda value: value and "padding-top: 50px;" in value and "padding-left: 100px;" in value and "padding-right: 100px;" in value and "margin-bottom: 10px;" in value)

        if content_div:
            # Extract text content
            text_content = content_div.get_text(strip=False)
            logging.info("Scraped text successfully.")
            return text_content
        else:
            logging.error("Could not find the content section on the page with the specified styles.")
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while making the request: {e}")
        return None

# Execute the function and publish to MQTT
if __name__ == "__main__":
    text = scrape_roturas()
    if text:
        logging.info(f"Scraped text: {text}")