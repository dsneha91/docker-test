CREATE DATABASE persons;
use persons;

CREATE TABLE all_persons (
  name VARCHAR(20),
  country VARCHAR(20)
);

INSERT INTO all_persons
  (name, country)
VALUES
  ('Meryll Streep', 'USA'),
  ('Roger Federer', 'Switzerland'),
  ('Morgan Freeman', 'USA'),
  ('Cristiano Ronaldo', 'Portugal'),
  ('Stephen Hawking', 'USA'),
  ('Jeff Bezzos', 'USA');
