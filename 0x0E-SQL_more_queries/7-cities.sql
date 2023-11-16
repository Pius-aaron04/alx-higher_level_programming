-- creates cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
id INT PRIMARY KEY,
state_id INT FOREIGN KEY(id) REFERENCES states(id),
name VARCHAR(256) NOT NULL
);
