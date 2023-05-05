FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./SkyPro_CourseWork_5 .

RUN gunicorn --bind 0.0.0.0:5000 wsgi:app