FROM python:3.8
RUN pip install kafka-python
COPY kafkatest.py /app/main.py
ENTRYPOINT ["python3", "/app/main.py"]
