DROP TABLE IF EXISTS bookings;
-- DROP TABLE IF EXISTS slots;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS courts;


CREATE TABLE courts (
    id SERIAL PRIMARY KEY,
    court_no INT,
    surface VARCHAR(255),
    capacity INT
);

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

-- CREATE TABLE slots (
--     id SERIAL PRIMARY KEY,
--     court_id INT REFERENCES courts(id) ON DELETE CASCADE,
--     start_time TIMESTAMP NOT NULL,
--     end_time TIMESTAMP NOT NULL,
--     available BOOLEAN NOT NULL DEFAULT TRUE
-- );





CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    -- slot_id  INT REFERENCES slots(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    court_id INT REFERENCES courts(id) ON DELETE CASCADE

    -- UNIQUE (slot_id, member_id)    
    
);
