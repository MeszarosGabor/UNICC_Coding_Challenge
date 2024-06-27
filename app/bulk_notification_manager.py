import collections
import typing

import app.notification_manager as notification_manager


def batch_notification_manager_single_threaded(
        payload: typing.List[typing.Dict]) -> typing.Dict:
    """
    This is a single threaded notification manager that attempts
    to send the notifications and reports the outcomes.
    """

    stats = collections.defaultdict(int)
    for item in payload:
        try:
            outcome = notification_manager.send_single_notification(item)
            stats[outcome] += 1
        except Exception as exc:
            # We do not want to re-raise to make sure an unexpected error
            # will not block the processing of the remaining items.
            # We nevertheless report the anomaly.
            stats[str(exc)] += 1

    return stats
