FROM python:latest

LABEL maintainer="nick_cramer@outlook.com"

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./apitest /automation/apitest
COPY ./setup.py /automation
COPY ./env_docker.sh /automation

WORKDIR /automation

RUN python3 setup.py install

