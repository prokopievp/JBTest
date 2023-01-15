FROM python:alpine

WORKDIR /JBtest
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY . .



