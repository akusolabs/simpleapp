FROM ubuntu:latest

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 -p 8080



