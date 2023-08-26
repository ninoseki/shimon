# build env
FROM node:20-alpine as build

COPY ./frontend /frontend

WORKDIR /frontend

RUN npm install \
  && npm run build \
  && rm -rf node_modules

# prod env
FROM python:3.11-alpine

RUN apk --no-cache add whois build-base libffi-dev

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock requirements.txt ./
COPY gunicorn.conf.py ./
COPY backend ./backend

RUN pip install --no-cache-dir -r requirements.txt \
  && poetry install --without dev

COPY --from=build /frontend ./frontend

ENV PORT 8000

EXPOSE $PORT

CMD ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "backend.main:app"]
