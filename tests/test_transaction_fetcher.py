import pytest
import requests
import responses

import app.constants as constants
import app.transaction_fetcher as transaction_fetcher


@responses.activate
def test_fetch_transaction_info__success():
    mock_json = [
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": "email",
        },
        {
            "name": "Jonathan Green",
            "email": "rpope@example.com",
            "phone": "(245)765-5361x8165",
            "url": None,
            "type": "email",
        },
    ]
    responses.add(
        responses.GET,
        constants.TRANSACTION_RAW_URL,
        json=mock_json,
        status=200,
    )
    resp = transaction_fetcher.fetch_transaction_info()

    assert resp == mock_json


@responses.activate
def test_fetch_transaction_info__connection_error():
    responses.add(responses.GET, constants.TRANSACTION_RAW_URL, status=500)
    with pytest.raises(requests.exceptions.HTTPError):
        transaction_fetcher.fetch_transaction_info()
