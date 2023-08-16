-- Lists all the names and scores in the second_table
-- where the score is greater than or equal to 10.
-- The results are sorted by score in descending order.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC
