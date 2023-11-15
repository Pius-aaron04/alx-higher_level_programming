-- Computes the score of all records in second_table
SELECT SUM(score) / COUNT(*) AS average
FROM second_table;
