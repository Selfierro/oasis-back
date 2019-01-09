FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y git libpq-dev libxslt-dev libxml2-dev libpam-dev libedit-dev tk-dev tcl-dev libcurl4-openssl-dev curl libssl-dev

RUN mkdir /code
WORKDIR /code

ADD requirements/base.txt /code/requirements/base.txt
RUN pip install -r requirements/base.txt

ADD . /code/