CREATE TABLE IF NOT EXISTS staging_posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT
);
