import base64
import mmh3
from urllib.parse import urlparse
from flask import Flask, request, render_template
import requests


def validate_url(url):
    valid_paths = ["", "/", "/favicon.ico"]
    url = urlparse(url)
    return url.path in valid_paths


def filter_type(url):
    url = urlparse(url)
    if url.path == "/favicon.ico":
        return "http.favicon.hash"
    else:
        return "http.html_hash"


def mmh3_hash(url):
    response = requests.get(url)
    response.raise_for_status()

    content_type = response.headers['Content-Type']
    if "text/html" in content_type:
        return mmh3.hash(response.text)
    else:
        b64 = base64.encodebytes(response.content)
        return mmh3.hash(b64)


app = Flask(__name__,
            static_folder="../dist/static",
            template_folder="../dist")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hash')
def hash():
    url = request.args.get("url", "http://example.com/")
    if not validate_url(url):
        return {"url": url, "error": "Invalid URL is given"}, 400

    type = filter_type(url)
    try:
        hash = mmh3_hash(url)
        return {"url": url, "type": type, "hash": hash}
    except Exception as error:
        return {"url": url, "error": str(error)}, 400
