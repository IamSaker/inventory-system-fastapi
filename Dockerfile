FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10
LABEL maintainer="Saker <iamsaker.s001@gmail.com>"

RUN apk update && apk upgrade && \
    apk add --no-cache libpq && \
    apk add --no-cache --virtual .build-deps \
      gcc \
      python3-dev \
      openssl-dev \
      musl-dev \
      postgresql-dev \
      libffi-dev

COPY ./app/requirements.txt /app/requirements.txt
RUN  pip install --no-cache-dir -r requirements.txt && \
     apk del .build-deps

COPY ./app ./app

RUN adduser -D inventory
RUN chown -R inventory:inventory /app
USER inventory

RUN python -m compileall .

ENV PORT 5000
ENV BIND 0.0.0.0:5000

EXPOSE 5000