"""
This is the main application component responsible for fetching the contacts
data and sending the appropriate notifications.
"""
import logging

import app.bulk_notification_manager as bulk_notification_manager
import app.transaction_fetcher as transaction_fetcher


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def main():
    logger.info("Started Transaction fetching...")
    transactions = transaction_fetcher.fetch_transaction_info_ram_optimized()
    logger.info("Comleted.Started notifications...")
    stats = bulk_notification_manager.batch_notification_manager_multi_threaded(transactions)  # noqa E501
    logger.info("Completed. Statistics:")
    for k, v in stats.items():
        logger.info(f"{k}: {v}")


if __name__ == "__main__":
    main()
