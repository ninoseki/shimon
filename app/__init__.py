from flask import Flask, request, render_template
from urllib.parse import urlparse
import base64
import mmh3
import requests


def validate_url(url) -> bool:
    valid_paths = ["", "/", "/favicon.ico"]
    url = urlparse(url)
    return url.path in valid_paths


def filter_type(url) -> str:
    url = urlparse(url)
    if url.path == "/favicon.ico":
        return "http.favicon.hash"
    else:
        return "http.html_hash"


def mmh3_hash(url) -> int:
    response = requests.get(url, verify=False)
    response.raise_for_status()

    content_type = response.headers["Content-Type"]
    if "text/html" in content_type:
        return mmh3.hash(response.text)
    else:
        b64 = base64.encodebytes(response.content)
        return mmh3.hash(b64)


app = Flask(
    __name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist",
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hash")
def hash():
    url = request.args.get("url")
    if url is None:
        return {"url": url, "error": "URL is not given"}, 400

    if not validate_url(url):
        return {"url": url, "error": "Invalid URL is given"}, 400

    type = filter_type(url)
    try:
        hash = mmh3_hash(url)
        return {"url": url, "type": type, "hash": hash}
    except requests.exceptions.HTTPError:
        return {"url": url, "error": "HTTP error"}, 400
    except requests.exceptions.ConnectionError:
        return {"url": url, "error": "Connection error"}, 400
    except requests.exceptions.Timeout:
        return {"url": url, "error": "Timeout error"}, 400
    except requests.exceptions.RequestException:
        return {"url": url, "error": "Request exception"}, 400
    except Exception as error:
        return {"url": url, "error": str(error)}, 400
