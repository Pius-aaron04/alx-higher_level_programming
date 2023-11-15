-- Full table creation
	CREATE TABLE IF NOT EXISTS second_table (
		id INT,
		name VARCHAR(256),
		score INT
	);

	-- insert sample rows
	INSERT INTO IF NOT EXISTS second_table
	VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Alex', 14),
	(4, 'Alex', 8);
