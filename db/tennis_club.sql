DROP TABLE bookings;
DROP TABLE members;
DROP TABLE courts;


CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(255),
    tel_no VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    dob VARCHAR(255),
    premium BOOLEAN,
    win INT,
    loss INT
);

CREATE TABLE courts (
    id SERIAL PRIMARY KEY,
    court_no INT,
    surface VARCHAR(255)

);




CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    court_id INT REFERENCES courts(id) ON DELETE CASCADE
    
);
