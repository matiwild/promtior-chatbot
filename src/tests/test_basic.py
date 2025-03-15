import unittest
from src.data_loader import load_document
from src.config import DOCUMENT_PATH

class TestDataLoader(unittest.TestCase):
    def test_load_document(self):
        text = load_document(DOCUMENT_PATH)
        self.assertTrue(len(text) > 0, "The document should not be empty.")

if __name__ == '__main__':
    unittest.main()
