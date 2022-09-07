-- Lists all cities contained in the database hbtn_0d_usa sorted in ascending order by cities.id.
-- Each record should display: cities.id - cities.name - states.name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id
ORDER BY cities.id ASC;
