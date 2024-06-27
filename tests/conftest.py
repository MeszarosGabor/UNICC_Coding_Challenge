import pytest


@pytest.fixture
def payload_all_fields_present():
    return {
        "name": "Brent Valdez",
        "email": "annagregory@example.org",
        "phone": "139.386.6589",
        "url": "https://ayers-perry.com/",
        "type": "email",
    }
