FROM python:3.11

WORKDIR /mysite

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt
COPY . .
