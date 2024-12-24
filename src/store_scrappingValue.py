import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def save_scraped_text(file_path, text, found_time=None):
    """
    Save the scraped text to a file along with the datetime when it was first found.
    
    Args:
        file_path (str): Path to the file where the text will be saved.
        text (str): The scraped text to save.
        found_time (str): The datetime when the text was first found. If None, use the current datetime.
    """
    if found_time is None:
        found_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Found on: {found_time}\n{text}")
    logging.info(f"Saved scraped text to {file_path}")

def load_previous_scraped_text(file_path):
    """
    Load the previously saved scraped text and timestamp from a file.
    
    Args:
        file_path (str): Path to the file to read the text from.
    
    Returns:
        tuple: A tuple containing the datetime and the previously saved text,
               or (None, "") if the file doesn't exist.
    """
    if not os.path.exists(file_path):
        return None, ""

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if len(lines) < 2:
            return None, ""
        return lines[0].strip().replace("Found on: ", ""), "".join(lines[1:]).strip()

def isNewValue(previous_text, current_text):
    """
    Compare two pieces of text and return the differences.
    
    Args:
        previous_text (str): The previously saved text.
        current_text (str): The newly scraped text.
    
    Returns:
        bool: True if the texts are different, False otherwise.
    """
    return previous_text != current_text

def processValue(newValue):
    """
    Process the new scraped value by comparing it with the previous value and saving it if different.
    
    Args:
        newValue (str): The newly scraped text.
    """
    
    output_dir = "output"
    current_script_path = os.path.abspath(__file__)
    current_script_dir = os.path.dirname(current_script_path)
    parent_dir = os.path.dirname(current_script_dir)
    output_absolute_path = os.path.join(parent_dir, output_dir)
    
    os.makedirs(output_absolute_path, exist_ok=True)

    file_path = os.path.join(output_absolute_path, "scraped_text.txt")

    last_found_time, previous_scraped_text = load_previous_scraped_text(file_path)

    if last_found_time:
        logging.info(f"Last text was found on: {last_found_time}")

    if isNewValue(previous_scraped_text, newValue):
        save_scraped_text(file_path, newValue, last_found_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        logging.info("New value detected and saved.")
        return True
    else:
        logging.info("No new value detected.")
        return False