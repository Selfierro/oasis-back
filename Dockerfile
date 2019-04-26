FROM python:3.6-slim
MAINTAINER Aykol Koykelov "kolyakoikelov@gmail.com"
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y git libpq-dev libxslt-dev libxml2-dev libpam-dev libedit-dev tk-dev tcl-dev libcurl4-openssl-dev curl libssl-dev nginx supervisor

RUN mkdir /code
WORKDIR /code

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY production/docker_nginx.conf /etc/nginx/sites-available/default
COPY production/docker_supervisor.conf /etc/supervisor/conf.d/

ADD requirements/base.txt /code/requirements/base.txt
RUN pip install -r requirements/base.txt

ADD . /code/

EXPOSE 80
EXPOSE 443

CMD ["supervisord", "-n"]