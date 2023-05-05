FROM python:3.10-slim

WORKDIR /code
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY .. .

CMD gunicorn --bind 0.0.0.0:80 -w 4 wsgi:app