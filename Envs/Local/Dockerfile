FROM python:3.11.1-slim

## ENVS variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

## System dependencies
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
RUN rm -rf /var/lib/apt/lists/*

## Project dependencies
COPY ./Envs/Local/requirements.txt /tmp/Requirements/Local/
COPY ./Envs/default_requirements.txt /tmp/Requirements/
COPY ./Envs/format_requirements.txt /tmp/Requirements/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/Requirements/Local/requirements.txt
RUN rm -r -f /tmp/Requirements

## Project files
RUN mkdir -p /App/
COPY ./Project /App/Project
COPY ./manage.py /App/
COPY ./Apps /App/Apps
COPY ./Envs/__init__.py /App/Envs/__init__.py
COPY ./Envs/Local/__init__.py /App/Envs/Local/__init__.py
COPY ./Envs/Local/django_settings.py /App/Envs/Local/django_settings.py
WORKDIR /App
