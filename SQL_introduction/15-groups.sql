-- lists the number of records with the same score in second_table
SELECT score, COUNT(*) AS num FROM second_table GROUP by score;
