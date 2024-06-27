import pytest


@pytest.fixture
def payload_single_item_all_fields_present():
    return {
        "name": "Brent Valdez",
        "email": "annagregory@example.org",
        "phone": "139.386.6589",
        "url": "https://ayers-perry.com/",
        "type": "email",
    }


@pytest.fixture
def payload_full_range():
    return [
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": "email",
        },
        {
            "name": None,
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": "email",
        },
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": None,
        },
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": "telepathy",
        },
        {
            "name": "Brent Valdez",
            "email": None,
            "phone": "139.386.6589",
            "url": "https://ayers-perry.com/",
            "type": "email",
        },
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": None,
            "url": "https://ayers-perry.com/",
            "type": "sms",
        },
        {
            "name": "Brent Valdez",
            "email": "annagregory@example.org",
            "phone": "139.386.6589",
            "url": None,
            "type": "post",
        },
    ]
