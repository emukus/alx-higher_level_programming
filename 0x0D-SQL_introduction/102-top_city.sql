-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Temps located in temperatures.sql
SELECT city, AVG(value) AS avg_temp from temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
