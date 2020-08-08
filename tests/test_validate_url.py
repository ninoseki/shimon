from app.api.endpoints.hashes import validate_url


def test_validate_url():
    assert validate_url("http://example.com") is True
    assert validate_url("http://example.com/") is True

    assert validate_url("http://example.com/favicon.ico") is True
    assert validate_url("http://example.com/favicon.png") is True
    assert validate_url("http://example.com/touch-icon.png") is True

    assert validate_url("http://example.com/foo/favicon.ico") is True
    assert validate_url("http://example.com/foo/bar/favicon.ico") is True

    assert validate_url("http://example.com/foo/bar") is False
    assert validate_url("foo") is False
