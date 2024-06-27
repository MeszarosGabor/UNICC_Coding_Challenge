import app.constants as constants
import app.bulk_notification_manager as bulk_notification_manager


def test_batch_notification_manager_single_threaded(payload_full_range):
    outcomes = (
        bulk_notification_manager.batch_notification_manager_single_threaded(
            payload_full_range
            )
    )

    assert outcomes == {
        constants.PayloadValidationResult.VALID_PAYLOAD: 1,
        constants.PayloadValidationResult.MISSING_NAME: 1,
        constants.PayloadValidationResult.MISSING_NOTIFICATION_TYPE: 1,
        constants.PayloadValidationResult.INVALID_NOTIFICATION_TYPE: 1,
        constants.PayloadValidationResult.MISSING_CONTACT_OF_NOTIFICATION_TYPE: 3,  # noqa E501
    }


def test_batch_notification_manager_single_threaded__unexpected_exception(
    mocker,
    payload_single_item_all_fields_present,
):
    mocker.patch(
        "app.notification_manager.send_single_notification",
        side_effect=ValueError("ValueError"),
    )

    outcomes = (
        bulk_notification_manager.batch_notification_manager_single_threaded(
            [payload_single_item_all_fields_present]
        )
    )

    assert outcomes == {"ValueError": 1}
