\c postgres
DROP TABLE IF EXISTS sites;

CREATE TABLE IF NOT EXISTS sites (
    id serial not null, 
    title varchar not null, 
    info varchar not null,
    timestamp timestamp default current_timestamp
    );