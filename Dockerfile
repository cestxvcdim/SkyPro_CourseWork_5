FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN gunicorn --bind 0.0.0.0:5000 app.py:app