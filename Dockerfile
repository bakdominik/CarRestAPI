# syntax=docker/dockerfile:1
FROM python:3.9.7-slim-buster
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
COPY requirements.txt /app/
RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser myuser
USER myuser

# run gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT