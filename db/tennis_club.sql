DROP TABLE members;
DROP TABLE courts;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN
);

CREATE TABLE courts (
    id SERIAL PRIMARY KEY,
    court_no INT,
    surface VARCHAR(255)

);
