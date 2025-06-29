CREATE TABLE IF NOT EXISTS staging_users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    email VARCHAR(255),
    address TEXT,
    phone VARCHAR(255),
    website VARCHAR(255),
    company TEXT
);
