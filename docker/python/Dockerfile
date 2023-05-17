FROM python:3.10

WORKDIR /app

RUN pip install gunicorn

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT "./docker/python/entrypoint.sh"
