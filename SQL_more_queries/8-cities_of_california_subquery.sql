-- lists all cities of California found in the database hbtn_0d_usa
SELECT cities.id, cities.name WHERE state.state_id = state.id ORDER BY cities.id ASC;
