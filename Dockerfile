FROM ubuntu:latest
# RUN apt-get update -y
# RUN apt-get install -y python3-dev python-pip
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y
RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["simpleapp.py"]


