# Dockerfile, Image, Container

FROM python:3.9.7

ADD main.py .
ADD scraper.py .
ADD db.py .
ADD requirements.txt .

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py"]

# docker build -t lux_project .
# docker run -p 8000:8000 lux_project
# docker exec -t 739db4ba20b7 /bin/sh