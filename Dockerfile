# Dockerfile, Image, Container

FROM python:3.9.7

ADD . / lux_project/

#SPLASH_URL = 'http://127.0.0.1:8080'

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#CMD [ "scrapy", "startscraper", "scraper" ]
#CMD ["scrapy", "crawl", "sreality"]
CMD [ "python", "/lux_project/main.py"]

# docker build --rm -t lux_project .       # build the lux_project image
# docker run -p 8080:8080 lux_project      # run the file
# docker exec -t <container-id> /bin/sh    # run a terminal