FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install psycopg2-binary kafka-python requests\
    pip install python-dotenv

COPY data_subscriber.py data_subscriber.py
COPY .env .env

ENTRYPOINT ["python", "data_subscriber.py"]