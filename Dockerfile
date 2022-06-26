# Dockerfile, Image, Container

FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip
RUN apt install -y libpq-dev

COPY scraper/ /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install --with-deps chromium


# TODO change this so it runs an instance where we can run a browser for scraping
# FROM python:3.9.7

#ADD . / lux_project/
# ADD . /scraper /

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# RUN yum -y install libappindicator-gtk3
# RUN yum -y install liberation-fonts
# RUN playwright install

#WORKDIR /

CMD ["scrapy", "crawl", "sreality"]
#CMD [ "python", "/lux_project/main.py"]

# docker build --rm -t lux_project .       # build the lux_project image
# docker run -p 8080:8080 lux_project      # run the image
# docker exec -t <container-id> /bin/sh    # run a terminal
# docker-compose up                        # run the whole shebang