import logging


def load_document(path: str) -> str:
    """Load the content of a text file."""
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        logging.error("Error loading document: %s", e)
        raise
