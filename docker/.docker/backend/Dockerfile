# Dockerfile, Image, Container

FROM python:3.9.7
ADD ./backend backend/
COPY ./wait-for-it.sh /backend/scraper

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/backend/"

WORKDIR /backend/scraper

# WORKDIR /app/website
# CMD scrapy crawl quotes;

RUN chmod +x ./wait-for-it.sh
CMD ["./wait-for-it.sh", "postgres:5432", "-t", "20", "--", "scrapy", "crawl", "quotes"]