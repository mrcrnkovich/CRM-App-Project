FROM python:3.8

WORKDIR /app

COPY requirements.txt /

RUN apt-get update; pip install --upgrade pip

RUN pip install --no-cache-dir -r /requirements.txt

CMD python3 test.py

