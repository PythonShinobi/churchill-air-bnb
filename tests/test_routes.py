
import pytest

from run import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_homepage_loads_successfully(client):
    response = client.get("/")

    assert response.status_code == 200


def test_homepage_contains_business_name(client):
    response = client.get("/")

    assert b"Churchil BnB" in response.data


def test_homepage_contains_main_sections(client):
    response = client.get("/")

    page = response.data.decode("utf-8")

    expected_sections = [
        "Home",
        "About",
        "Amenities",
        "Gallery",
        "Location",
    ]

    for section in expected_sections:
        assert section in page


def test_homepage_contains_hero_heading(client):
    response = client.get("/")

    assert b"Your Home Away From Home" in response.data


def test_contact_number_is_correct(client):
    response = client.get("/")

    page = response.data.decode("utf-8")

    assert "+254 734 332727" in page
    assert 'href="tel:+254734332727"' in page


def test_location_contains_tudor_mombasa(client):
    response = client.get("/")

    page = response.data.decode("utf-8")

    assert "Tudor" in page
    assert "Mombasa" in page
    assert "maps.google.com" in page


def test_stylesheet_loads(client):
    response = client.get("/static/css/style.css")

    assert response.status_code == 200
    assert b"body" in response.data


def test_javascript_loads(client):
    response = client.get("/static/js/main.js")

    assert response.status_code == 200
