import unittest
from src import store_scrappingValue

class TestStoreScrappingValue(unittest.TestCase):

    def test_is_new_value(self):
        self.assertTrue(store_scrappingValue.isNewValue("old text", "new text"))
        self.assertFalse(store_scrappingValue.isNewValue("same text", "same text"))

    def test_save_and_load_scraped_text(self):
        file_path = "test_scraped_text.txt"
        text = "Test text"
        store_scrappingValue.save_scraped_text(file_path, text)
        found_time, loaded_text = store_scrappingValue.load_previous_scraped_text(file_path)
        self.assertEqual(text, loaded_text)

if __name__ == "__main__":
    unittest.main()