FROM python:latest

WORKDIR /api

COPY *.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "api.py"]
