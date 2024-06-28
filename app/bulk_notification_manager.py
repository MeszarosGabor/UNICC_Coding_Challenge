import collections
import more_itertools
import typing
from concurrent.futures import ThreadPoolExecutor

import app.constants as constants
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


def batch_notification_manager_multi_threaded(
        payload: typing.List[typing.Dict]) -> typing.Dict:

    stats = collections.defaultdict(int)
    with ThreadPoolExecutor(
            max_workers=constants.MULTITHREADING_MAX_WORKERS) as executor:
        for batch in more_itertools.ichunked(
                payload, constants.MULTITHREADING_MAX_WORKERS):
            futures = [executor.submit(
                notification_manager.send_single_notification, item)
                for item in batch
            ]
            for future in futures:
                stats[future.result()] += 1

    return stats
