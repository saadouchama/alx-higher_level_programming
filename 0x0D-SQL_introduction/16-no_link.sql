-- Lists socre and names from second_table
-- where name is not empty or null
-- and orders them by score in descending order
SELECT score, name FROM second_table
WHERE name != "" AND name IS NOT NULL
ORDER BY score DESC;
