# Dockerfile, Image, Container

FROM python:3.9.7
ADD . / /
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD python -m http.server 8000
