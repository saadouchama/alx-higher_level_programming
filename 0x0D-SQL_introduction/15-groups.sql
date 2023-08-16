-- Lists the number of records with the same score in the 'second_table' table
-- the result should display the score and the number of records with the label 'number'
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
