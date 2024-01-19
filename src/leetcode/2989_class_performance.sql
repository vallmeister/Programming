WITH t1 AS(
    SELECT assignment1 + assignment2 + assignment3 as score
    FROM Scores)
SELECT MAX(score) - MIN(score) as difference_in_score
FROM t1