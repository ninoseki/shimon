# Frontend
FROM node:20-alpine3.18 as frontend

WORKDIR /usr/src/app

COPY ./frontend ./frontend

WORKDIR /usr/src/app/frontend

RUN npm install && npm run build && rm -rf node_modules

# Backend
FROM python:3.11-slim-bookworm as backend

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && apt-get clean  \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-root --without dev

# Main
FROM python:3.11-slim-bookworm

COPY --from=backend /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=backend /usr/local/bin/ /usr/local/bin/

WORKDIR /usr/src/app

COPY gunicorn.conf.py ./
COPY backend ./backend
COPY --from=frontend /usr/src/app/frontend ./frontend

EXPOSE $PORT

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "backend.main:app"]
