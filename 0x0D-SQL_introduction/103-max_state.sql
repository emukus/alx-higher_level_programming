-- Displays the max temperature of each state (ordered by State name).
-- Temps located in temperatures.sql
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state
ORDER BY state;
