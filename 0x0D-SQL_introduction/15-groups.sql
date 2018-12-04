-- prints the sores and the number of rows that have that score
SiELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
