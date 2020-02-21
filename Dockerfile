FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /goodbuy-django-docker
WORKDIR /goodbuy-django-docker
COPY requirements.txt /goodbuy-django-docker/
RUN apt-get -y update && apt-get install -y libzbar-dev
RUN pip install -r requirements.txt
COPY . /goodbuy-django-docker/
