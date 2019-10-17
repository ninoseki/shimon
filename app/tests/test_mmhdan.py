from app import app, validate_url, filter_type
import pytest


def test_validate_url():
    assert validate_url("http://example.com") is True
    assert validate_url("http://example.com/") is True
    assert validate_url("http://example.com/favicon.ico") is True

    assert validate_url("http://example.com/foo/bar") is False
    assert validate_url("foo") is False


def test_filter_type():
    assert filter_type("http://example.com") == "http.html_hash"
    assert filter_type(
        "http://example.com/favicon.ico") == "http.favicon.hash"


def test_index(client):
    rv = client.get("/")
    assert rv.status_code == 200


@pytest.fixture
def client(mocker):
    app.config["TESTING"] = True

    mocker.patch("app.mmh3_hash", return_value="foo bar")

    return app.test_client()


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_hash_with_valid_inputs(client):
    resp = client.get("/hash?url=http://example.com")
    assert resp.status_code == 200

    resp = client.get("/hash?url=http://example.com/favicon.ico")
    assert resp.status_code == 200


def test_hash_with_invalid_inputs(client):
    resp = client.get("/hash?url=http://example.com/foo")
    assert resp.status_code == 400

    resp = client.get("/hash?url=http://example.com/foo/bar")
    assert resp.status_code == 400

    resp = client.get("/hash?foo=bar")
    assert resp.status_code == 400

    resp = client.get("/hash")
    assert resp.status_code == 400
