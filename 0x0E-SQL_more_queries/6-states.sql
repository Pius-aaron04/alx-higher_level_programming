-- creates a database and a table with id as primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
id INT PRIMARY KEY,
name VARCHAR(256) NOT NULL
);