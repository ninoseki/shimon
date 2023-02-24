# build env
FROM node:18-alpine as build

COPY ./frontend /frontend
WORKDIR /frontend
ENV NODE_OPTIONS --openssl-legacy-provider
RUN npm install && npm run build && rm -rf node_modules

# prod env
FROM python:3.11-alpine

RUN apk --no-cache add whois build-base libffi-dev

WORKDIR /backend

COPY pyproject.toml poetry.lock requirements.txt /backend/
COPY gunicorn.conf.py /backend/
COPY app /backend/app

RUN pip install --no-cache-dir -r requirements.txt \
  && poetry install --without dev

COPY --from=build /frontend /backend/frontend

ENV PORT 8000

EXPOSE $PORT

CMD poetry run gunicorn -k uvicorn.workers.UvicornWorker app.main:app