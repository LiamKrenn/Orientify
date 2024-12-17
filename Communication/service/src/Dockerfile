FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY service.py service.py
COPY calculation.py calculation.py

CMD ["python", "service.py"]
