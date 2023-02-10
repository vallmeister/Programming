SELECT gender, Scores.day, SUM(score_points) OVER(PARTITION BY gender ORDER BY Scores.day) AS total
FROM Scores
