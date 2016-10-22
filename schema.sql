CREATE TABLE if not exists data (
    time  DATETIME PRIMARY KEY,
    light BOOLEAN,
    acc REAL,
    tmp REAL,
    baro REAL
);
