DROP TABLE IF EXISTS posts; --so 2 databases can't exist at once

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- NOT NULL means cant be left blank
    title TEXT NOT NULL,
    content TEXT NOT NULL
);