FROM amd64/python:3.9-slim

WORKDIR /usr/app

RUN pip install -U pip \
    && pip install "fastapi[all]"

COPY CRUD_Pydantic.py CRUD_Pydantic.py

CMD ["uvicorn", "CRUD_Pydantic:app", "--host", "0.0.0.0", "--reload"]