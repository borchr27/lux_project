# Dockerfile, Image, Container

# TODO change this so it runs an instance where we can run a browser for scraping
FROM python:3.9.7

#ADD . / lux_project/
ADD . /scraper /

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN yum -y install libappindicator-gtk3
# RUN yum -y install liberation-fonts
RUN playwright install

WORKDIR /

CMD ["scrapy", "crawl", "sreality"]
#CMD [ "python", "/lux_project/main.py"]

# docker build --rm -t lux_project .       # build the lux_project image
# docker run -p 8080:8080 lux_project      # run the image
# docker exec -t <container-id> /bin/sh    # run a terminal
# docker-compose up                        # run the whole shebang