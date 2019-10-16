from app import validate_url, filter_type


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
