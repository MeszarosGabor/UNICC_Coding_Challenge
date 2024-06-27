import pytest

import app.constants as constants
import app.notification_manager as notification_manager


@pytest.mark.parametrize(
    "contact_type",
    [
        pytest.param("email"),
        pytest.param("phone"),
        pytest.param("url"),
    ],
)
def test_send_single_notification__success(
    contact_type, mocker, payload_all_fields_present
):
    payload_all_fields_present["type"] = contact_type
    mocked_interface = mocker.patch(
        "app.interface_utils."
        f"{notification_manager.CONTACT_MECHANISM[contact_type].__name__}"
    )
    notification_manager.CONTACT_MECHANISM[contact_type] = mocked_interface

    outcome = notification_manager.send_single_notification(
        payload=payload_all_fields_present
    )
    assert outcome == constants.PayloadValidationResult.VALID_PAYLOAD
    mocked_interface.assert_called_once()


def test_send_single_notification__missing_notification_type(
    payload_all_fields_present,
):
    payload_all_fields_present["type"] = None

    outcome = notification_manager.send_single_notification(
        payload=payload_all_fields_present
    )
    assert (
        outcome == constants.PayloadValidationResult.MISSING_NOTIFICATION_TYPE
    )


def test_send_single_notification__invalid_notification_type(
    payload_all_fields_present,
):
    payload_all_fields_present["type"] = "telephathy"

    outcome = notification_manager.send_single_notification(
        payload=payload_all_fields_present
    )
    assert (
        outcome == constants.PayloadValidationResult.INVALID_NOTIFICATION_TYPE
    )


@pytest.mark.parametrize(
    "contact_type",
    [
        pytest.param("email"),
        pytest.param("phone"),
        pytest.param("url"),
    ],
)
def test_send_single_notification__missing_contact_of_notification_type(
    contact_type, payload_all_fields_present
):
    payload_all_fields_present["type"] = contact_type
    payload_all_fields_present[contact_type] = None

    outcome = notification_manager.send_single_notification(
        payload=payload_all_fields_present
    )
    assert (
        outcome ==
        constants.PayloadValidationResult.MISSING_CONTACT_OF_NOTIFICATION_TYPE
    )
