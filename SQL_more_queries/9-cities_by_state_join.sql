-- Lists each city with its state name, sorted by cities.id.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
