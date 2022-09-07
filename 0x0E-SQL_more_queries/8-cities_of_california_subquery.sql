-- Lists all the cities of California that can be found in the database hbtn_0d_usa sorted in ascending order by cities.id.
-- The states table contains only one record where name = California (but the id can be different)
-- not allowed to use the JOIN keyword.
SELECT id, name FROM cities
WHERE state_id IN
(
	SELECT id FROM states
	WHERE name = 'California'
)
ORDER BY id;

