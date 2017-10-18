FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers pkgconf \
    autoconf automake libtool make postgresql-dev postgresql-client openssl-dev && \
    apk add bash postgresql-libs postgresql-client && \
    (while true; do pip --no-cache-dir install uwsgi && break; done)

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ARG SECRET_KEY="9z1&pn!+6x@#7w^vr8z23&e82*5@^lo5%zpk7wygo)6bzx5(%a"
ENV SECRET_KEY $SECRET_KEY
RUN python ./manage.py collectstatic --noinput && \
    apk del .build-deps