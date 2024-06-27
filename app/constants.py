# flake8: noqa: E501
# NOTE: constants are likely to become long, we are going to ignore this flake8 check in this very file.

from enum import Enum


TRANSACTION_URL = "https://github.com/UN-ICC/notifications-processor/blob/master/notifications_log.json"
TRANSACTION_RAW_URL = TRANSACTION_URL.replace(
    "github.com", "raw.githubusercontent.com"
).replace("/blob/", "/")


class PayloadValidationResult(Enum):
    VALID_PAYLOAD = 0
    MISSING_NAME = 1
    MISSING_NOTIFICATION_TYPE = 2
    INVALID_NOTIFICATION_TYPE = 3
    MISSING_CONTACT_OF_NOTIFICATION_TYPE = 4
