import vcr


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/example.yaml", ignore_hosts=["testserver"]
)
def test_hash_with_valid_input1(client):
    resp = client.get("/api/hashes/calculate", params={"url": "http://example.com"})
    assert resp.status_code == 200

    data = resp.json()
    assert data.get("url") == "http://example.com/"
    assert data.get("contentType") == "text/html; charset=UTF-8"
    assert data.get("mmh3") == -2087618365
    assert data.get("md5") == "84238dfc8092e5d9c0dac8ef93371a07"
    assert (
        data.get("sha256")
        == "ea8fac7c65fb589b0d53560f5251f74f9e9b243478dcb6b3ea79b5e36449c8d9"
    )


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/google.yaml", ignore_hosts=["testserver"]
)
def test_hash_with_valid_input2(client):
    resp = client.get(
        "/api/hashes/calculate", params={"url": "https://www.google.com/favicon.ico"}
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data.get("url") == "https://www.google.com/favicon.ico"
    assert data.get("contentType") == "image/x-icon"
    assert data.get("mmh3") == 708578229
    assert data.get("md5") == "f3418a443e7d841097c714d69ec4bcb8"
    assert (
        data.get("sha256")
        == "6da5620880159634213e197fafca1dde0272153be3e4590818533fab8d040770"
    )


def test_hash_with_invalid_input1(client):
    # only the root ("/") or favicon is accepted
    resp = client.get("/api/hashes/calculate", params={"url": "http://example.com/foo"})
    assert resp.status_code == 400

    resp = client.get(
        "/api/hashes/calculate", params={"url": "http://example.com/foo/bar"}
    )
    assert resp.status_code == 400

    # http://example.com/favicon.ico returns 404
    resp = client.get(
        "/api/hashes/calculate", params={"url": "http://example.com/favicon.ico"}
    )
    assert resp.status_code == 500

    # foo is an invalid parameter
    resp = client.get("/api/hashes/calculate", params={"foo": "bar"})
    assert resp.status_code == 422

    # url parameter is missing
    resp = client.get("/api/hashes/calculate")
    assert resp.status_code == 422


@vcr.use_cassette("tests/fixtures/vcr_cassettes/404.yaml", ignore_hosts=["testserver"])
def test_hash_with_invalid_input2(client):
    # http://example.com/favicon.ico returns 404
    resp = client.get(
        "/api/hashes/calculate", params={"url": "http://example.com/favicon.ico"}
    )
    assert resp.status_code == 500
