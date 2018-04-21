FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./django/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./django /code/
