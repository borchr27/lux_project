# Dockerfile, Image, Container

FROM python:3.9.7
ADD . / app/

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/"

WORKDIR /app/scraper
# RUN scrapy crawl sreality
# CMD scrapy crawl sreality

# WORKDIR /app/website
CMD scrapy crawl quotes; cd ..; cd website; python main.py
# CMD [ "python", "/lux_project/main.py"]

# docker build --rm -t lux_project .       # build the lux_project image
# docker run -p 8080:8080 lux_project      # run the image
# docker exec -t <container-id> /bin/sh    # run a terminal
# docker-compose up                        # run the whole shebang