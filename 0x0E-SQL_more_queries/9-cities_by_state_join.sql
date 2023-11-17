-- lists all cities contained in the hbtn_0d_usa database
SELECT cities.id, cities.name, states.name
FROM cities
NATURAL JOIN states
ORDER BY states.id ASC;
