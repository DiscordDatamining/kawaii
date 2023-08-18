
CREATE TABLE IF NOT EXISTS cache (
    list TEXT
);

CREATE TABLE IF NOT EXISTS avatars (
    member BIGINT,
    avatar[] TEXT
);
