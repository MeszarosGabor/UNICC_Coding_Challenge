import logging
import os

import ijson
import requests

import app.constants as constants


logger = logging.getLogger(__name__)


def fetch_transaction_info():
    """
    Collects and returns the JSON content of the page.
    Assumes that the content can fit into memory!
    """
    response = requests.get(constants.TRANSACTION_RAW_URL)
    response.raise_for_status()

    return response.json()


def fetch_transaction_info_ram_optimized():
    temp_file_name = 'temp_notifications_log.json'
    response = requests.get(constants.TRANSACTION_RAW_URL, stream=True)
    response.raise_for_status()

    with open(temp_file_name, 'wb') as file:
        for chunk in response.iter_content(
                chunk_size=constants.DOWNLOAD_CHUNK_SIZE):
            if chunk:
                file.write(chunk)

    with open(temp_file_name, 'rb') as file:
        parser = ijson.parse(file)
        json_item = {}
        for prefix, event, value in parser:
            match prefix:
                case "item.name":
                    json_item["name"] = value
                case "item.email":
                    json_item["email"] = value
                case "item.phone":
                    json_item["phone"] = value
                case "item.url":
                    json_item["url"] = value
                case "item.type":
                    json_item["type"] = value
            if event == "end_map":
                yield json_item
                json_item = {}

    try:
        os.remove(temp_file_name)
        logger.info(f"{temp_file_name} has been deleted successfully.")
    except FileNotFoundError:
        logger.error(f"{temp_file_name} does not exist.")
    except PermissionError:
        logger.error(f"Permission denied: {temp_file_name}.")
    except Exception as e:
        logger.error(f"Error occurred while deleting {temp_file_name}: {e}")
