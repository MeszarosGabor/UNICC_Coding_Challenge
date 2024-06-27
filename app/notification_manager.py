import typing

import app.constants as constants
import app.interface_utils as interface_utils


CONTACT_MECHANISM = {
    "email": interface_utils.send_email,
    "sms": interface_utils.send_sms,
    "post": interface_utils.send_post,
}
CONTACT_TYPE_TO_DATA_KEY = {
    "email": "email",
    "sms": "phone",
    "post": "url",
}


NOTIFICATION_PAYLOAD = {"foo": "bar"}


def send_single_notification(
        payload: typing.Dict) -> constants.PayloadValidationResult:
    if not payload.get("name"):
        return constants.PayloadValidationResult.MISSING_NAME

    contact_type = payload.get("type")
    if not contact_type:
        return constants.PayloadValidationResult.MISSING_NOTIFICATION_TYPE
    if contact_type not in CONTACT_MECHANISM.keys():
        return constants.PayloadValidationResult.INVALID_NOTIFICATION_TYPE

    contact_info = payload.get(CONTACT_TYPE_TO_DATA_KEY[contact_type])
    if not contact_info:
        return constants.PayloadValidationResult.MISSING_CONTACT_OF_NOTIFICATION_TYPE  # noqa E501

    CONTACT_MECHANISM[contact_type](contact_info, NOTIFICATION_PAYLOAD)
    return constants.PayloadValidationResult.VALID_PAYLOAD
