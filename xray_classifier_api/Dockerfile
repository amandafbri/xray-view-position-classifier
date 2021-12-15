FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y git

COPY pyproject.toml poetry.lock /app/
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY xray_classifier_api /app/xray_classifier_api/

ENTRYPOINT [ "/bin/bash","/app/xray_classifier_api/entrypoint.sh" ]
