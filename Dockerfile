FROM ubuntu:focal
LABEL maintainer="redilonka@gmail.com"

RUN apt update -y && apt install -y python3-pip

RUN mkdir /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["pytest", "homework6/test_opencart.py"]
