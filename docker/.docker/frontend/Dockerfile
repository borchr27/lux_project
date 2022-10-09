# Dockerfile, Image, Container

FROM python:3.9.7
ADD ./frontend frontend/
COPY ./wait-for-it.sh /frontend

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/frontend/"

WORKDIR /frontend

CMD python main.py

# RUN chmod +x ./wait-for-it.sh
# CMD ["./wait-for-it.sh", "postgres:5432", "-t", "20", "--", "gunicorn", "-b", "0.0.0.0:8080", "main:app"]

# docker build --rm -t lux_project .       # build the lux_project image
# docker run -p 8080:8080 lux_project      # run the image
# docker exec -t <container-id> /bin/sh    # run a terminal
# docker-compose up                        # run the whole shebang