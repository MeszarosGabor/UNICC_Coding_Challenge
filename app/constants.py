# flake8: noqa: E501
# NOTE: constants are likely to become long, we are going to ignore this flake8 check in this very file.

TRANSACTION_URL = "https://github.com/UN-ICC/notifications-processor/blob/master/notifications_log.json"
TRANSACTION_RAW_URL = TRANSACTION_URL.replace(
    "github.com", "raw.githubusercontent.com"
).replace("/blob/", "/")
