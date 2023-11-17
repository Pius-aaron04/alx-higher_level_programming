-- lists all cities contained in the hbtn_0d_usa database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON states.id = cities.states_id
ORDER BY states.id ASC;
