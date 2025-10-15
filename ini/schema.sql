CREATE TABLE registry (
    id SERIAL PRIMARY KEY,
    car_plate VARCHAR(7) NOT NULL,
    proprietor VARCHAR(255) NOT NULL,
    model VARCHAR(255),
    entry_time TIMESTAMP,
    exit_time TIMESTAMP,
    value FLOAT4
);

CREATE TABLE system_config (
    id SERIAL PRIMARY KEY,
    "key" VARCHAR(50) NOT NULL UNIQUE,
    value FLOAT4
);

INSERT INTO system_config ("key", value)
VALUES
    ('value_peer_hour', 5.0)
