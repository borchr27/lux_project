# Python Web Scraper

This is a python web scraper proof of concept in docker using Postgres to store the scraped data then retrieve the data from the database, create a simple html page and display the data at `localhost:8080`.

## Setup

1. To run this project first make sure you have docker installed.
2. Clone this repository.
3. Navigate to the docker folder enclosed in the cloned file.
4. Run the `docker compose up --build` command.
5. Make sure the container is running and displays this message `backend exited with code 0`, this may take a minute or two.
6. Refresh the `docker_frontend` image in the docker dashboard. 
7. Navigate to `localhost:8080` in your browser.

You should now see the scraped text from the websites listed in the '/docker/backend/sites.csv' displayed on the page.