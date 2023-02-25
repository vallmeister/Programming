WITH t1 AS (
    SELECT *, SUM(CASE WHEN result = 'Win' THEN 0 ELSE 1 END) OVER (PARTITION BY player_id ORDER BY match_day) not_won
    FROM Matches
)
SELECT player_id, MAX(streak) AS longest_streak
FROM (SELECT player_id, SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) streak
      FROM t1
      GROUP BY player_id, not_won) t2
GROUP BY 1
