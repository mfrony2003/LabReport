# base image  
FROM python:3.12.0
ENV PYTHONUNBUFFERED 1  
WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt  


