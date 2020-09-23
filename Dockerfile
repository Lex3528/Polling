FROM python:3.7.4

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gdal-bin libgdal-dev python3-gdal binutils libproj-dev gcc python3-dev musl-dev

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./compose/django/django_start /django_start
RUN sed -i 's/\r//' /django_start
RUN chmod +x /django_start

