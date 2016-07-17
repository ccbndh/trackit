FROM ubuntu:16.04
MAINTAINER ccbn

RUN apt-get update --fix-missing && apt-get install -y supervisor
RUN apt-get install -y software-properties-common git libyaml-dev libpq-dev libxml2-dev libffi-dev libxslt1-dev python-dev python-setuptools apt-transport-https
RUN apt-get install -y python-pip
RUN apt-get install -y netcat-traditional
RUN apt-get install -y nodejs
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN apt-get install -y npm

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/code/ /var/log/celery /var/log/supervisor

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

CMD ["/usr/bin/supervisord"]
