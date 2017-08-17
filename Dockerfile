FROM vevende/python3:latest
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
EXPOSE 5000
ENV SERVER_HOST 0.0.0.0
ENV SERVER_PORT 5000
CMD ["python", "main.py"]