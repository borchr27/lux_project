# Dockerfile, Image, Container

FROM python:3.9.7
ADD . / app/
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app
CMD python main.py
# CMD python -m http.server 8000
