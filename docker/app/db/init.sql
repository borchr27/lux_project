\c docker;

DROP TABLE quotes;

CREATE TABLE IF NOT EXISTS quotes (
    id serial not null, 
    author text not null, 
    quote text not null
    );