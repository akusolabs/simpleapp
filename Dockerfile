FROM ubuntu:latest
<<<<<<< HEAD
# RUN apt-get update -y
# RUN apt-get install -y python3-dev python-pip
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y
RUN pip install --upgrade pip

=======
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
>>>>>>> master
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["simpleapp.py"]


