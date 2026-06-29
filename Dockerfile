FROM python:3.11-slim
LABEL maintainer="pislar33@gmail.com"
ENV PYTHONUNBUFERED 1
WORKDIR app/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ .
CMD ["python", "main.py"]