-- lists all cities of California found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND states.state_id = states.id 
ORDER BY cities.id ASC;
