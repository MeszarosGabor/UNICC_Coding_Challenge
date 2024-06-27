import requests

import app.constants as constants


def fetch_transaction_info():
    """
    Collects and returns the JSON content of the page.
    Assumes that the content can fit into memory!
    """
    response = requests.get(constants.TRANSACTION_RAW_URL)
    response.raise_for_status()

    return response.json()
