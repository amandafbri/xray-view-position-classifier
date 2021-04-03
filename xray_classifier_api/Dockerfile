FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y git

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY xray_classifier_api /app/

ENTRYPOINT [ "/bin/bash","/entrypoint.sh" ]
