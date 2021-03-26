import vcr
from fastapi.testclient import TestClient


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/example.yaml", ignore_hosts=["testserver"]
)
def test_example_com(client: TestClient):
    resp = client.get(
        "/api/fingerprint/calculate", params={"url": "http://example.com"}
    )
    assert resp.status_code == 200

    data = resp.json()

    html = data.get("html")
    assert html.get("url") == "http://example.com/"
    assert html.get("contentType") == "text/html; charset=UTF-8"
    assert html.get("mmh3") == -2087618365
    assert html.get("md5") == "84238dfc8092e5d9c0dac8ef93371a07"
    assert (
        html.get("sha256")
        == "ea8fac7c65fb589b0d53560f5251f74f9e9b243478dcb6b3ea79b5e36449c8d9"
    )

    assert data.get("favicon") is None
    assert data.get("certificate") is None


@vcr.use_cassette(
    "tests/fixtures/vcr_cassettes/https_example.yaml", ignore_hosts=["testserver"]
)
def test_https_example_com(client: TestClient):
    resp = client.get(
        "/api/fingerprint/calculate", params={"url": "https://example.com"}
    )
    assert resp.status_code == 200

    data = resp.json()
    assert data.get("certificate") is not None


def test_invalid_urls(client: TestClient):
    # only the root ("/") or favicon is accepted
    resp = client.get(
        "/api/fingerprint/calculate", params={"url": "http://example.com/foo"}
    )
    assert resp.status_code == 400

    resp = client.get(
        "/api/fingerprint/calculate", params={"url": "http://example.com/foo/bar"}
    )
    assert resp.status_code == 400

    # foo is an invalid parameter
    resp = client.get("/api/fingerprint/calculate", params={"foo": "bar"})
    assert resp.status_code == 422

    # url parameter is missing
    resp = client.get("/api/fingerprint/calculate")
    assert resp.status_code == 422
