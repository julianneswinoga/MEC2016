CREATE TABLE if not exists data (
    time  DATETIME PRIMARY KEY,
    longitude REAL,
    latitude REAL,
    light BOOLEAN,
    acc REAL,
    tmp REAL,
    baro REAL
);
