"""
This library summarizes the various (currently, mock) interface implementation.
"""


def send_sms(phone: str, data: dict) -> None:
    print(f"SMS sent to {phone}. Data: {data}")


def send_email(email: str, data: dict) -> None:
    print(f"EMAIL sent to {email}. Data: {data}")


def send_post(url: str, data: dict) -> None:
    print(f"POST sent to {url}. Data: {data}")
