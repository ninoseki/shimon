# mmhdan

![Python CI](https://github.com/ninoseki/mmhdan/workflows/Python%20CI/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ninoseki/mmhdan/badge.svg?branch=master)](https://coveralls.io/github/ninoseki/mmhdan?branch=master)

Calculate fingerprints of a website for OSINT search.

## Requirements

- Python 3.10
- Node.js v18

## Supported services

- BinaryEdge
- Censys
- DomainBigData
- DomainWatch
- Onyphe
- SecurityTrails
- Shodan
- SpyOnWeb
- Spyse
- urlscan.io
- VirusTotal
- ZoomEye

## Installation

```bash
git clone https://github.com/ninoseki/mmhdan.git

pip install -r requirements.txt

cd frontend
npm install
npm run build
```

## Dev server

```bash
uvicorn app:app
```

## Demo

* https://mmhdan.herokuapp.com/
