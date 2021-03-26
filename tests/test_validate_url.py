from app.api.endpoints.fingerprint import validate_url


def test_validate_url():
    assert validate_url("http://example.com") is True
    assert validate_url("http://example.com/") is True

    assert validate_url("http://example.com/foo/bar") is False
    assert validate_url("foo") is False
