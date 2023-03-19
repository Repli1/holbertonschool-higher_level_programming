-- lists all records of second_table, only rows with name value, score and name, descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
