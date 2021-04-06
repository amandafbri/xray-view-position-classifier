FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y git

COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir --compile

COPY xray_classifier_api /app/xray_classifier_api/

CMD ["python", "/xray_classifier_api/flask_api.py"]

# To run with Docker-Compose
# ENTRYPOINT [ "/bin/bash","/xray_classifier_api/entrypoint.sh" ]
