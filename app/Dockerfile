# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set PYTHONPATH to the repo root
ENV PYTHONPATH=/

WORKDIR /

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/
