FROM ubuntu:22.10

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt update; \
    apt install -y python3-pip; \
    apt install -y build-essential libssl-dev libffi-dev python3-dev; \
    python3 -m pip install ansible;
