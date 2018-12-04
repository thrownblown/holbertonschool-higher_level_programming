-- prints rows with names sorted by score from second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
