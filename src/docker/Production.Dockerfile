FROM python:3.6.3
ARG SERVER_HOST=0.0.0.0
ARG SERVER_PORT=5000

ENV SERVER_HOST=${SERVER_HOST}
ENV SERVER_PORT=${SERVER_PORT}

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

EXPOSE ${SERVER_PORT}
WORKDIR /App
COPY . /App
CMD ["python", "main.py"]