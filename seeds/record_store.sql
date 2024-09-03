-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO albums (title, release_year, artist_id) VALUES ('What Went Down', 2015, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Humbug', 2009, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Singles', 2014, 3);
-- INSERT INTO albums (title, release_year, artist_id) VALUES ('1989', 2014, 4);
-- INSERT INTO albums (title, release_year, artist_id) VALUES ('Tea For The Tillerman', 1970, 5);

