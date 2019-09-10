FROM python:3.6
#LABEL maintainer="hello@wagtail.io"

RUN apt-get update && apt-get install postgresql postgresql-contrib -y
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /src/requirements.txt
COPY wait-for.sh .
COPY docker_run.sh .
RUN pip install -U pip setuptools wheel
RUN pip install -r /src/requirements.txt
RUN pip install gunicorn

COPY . /src/
WORKDIR /src/
