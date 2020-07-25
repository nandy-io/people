FROM python:3.6.7-alpine3.7

RUN apk add git

RUN mkdir -p /opt/nandy-io

WORKDIR /opt/nandy-io

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD lib .
ADD test .
ADD setup.py .

ENV PYTHONPATH "/opt/nandy-io/lib:${PYTHONPATH}"
