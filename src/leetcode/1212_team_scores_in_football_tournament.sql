WITH cte AS (
    SELECT host_team, m.guest_team,
           CASE WHEN m.host_goals > m.guest_goals THEN 'host_win'
               WHEN m.host_goals = m.guest_goals THEN 'draw'
               WHEN m.host_goals < m.guest_goals THEN 'host_lose' END AS result
    FROM Matches m
),
cte2 AS (
    SELECT t1.team_id, t1.team_name,
           CASE WHEN cte.result = 'host_win' THEN 3
            WHEN cte.result = 'draw' THEN 1
            ELSE 0 END AS points
    FROM Teams t1
    LEFT JOIN cte ON t1.team_id = cte.host_team
    UNION ALL
    SELECT t2.team_id, t2.team_name,
           CASE WHEN cte.result = 'host_lose' THEN 3
            WHEN cte.result = 'draw' THEN 1
            ELSE 0 END AS points
    FROM Teams t2
    LEFT JOIN cte ON t2.team_id = cte.guest_team
)
SELECT team_id, team_name, SUM(points) num_points
FROM cte2
GROUP BY 1, 2
ORDER BY 3 DESC, 1
