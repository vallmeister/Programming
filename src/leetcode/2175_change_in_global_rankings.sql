WITH bef AS (
    SELECT *, RANK() OVER (ORDER BY points DESC, name) AS rk
    FROM TeamPoints
),
aft AS (
    SELECT t.team_id, t.name, t.points + p.points_change AS points,
           RANK() OVER (ORDER BY t.points + p.points_change DESC, name) AS rk
    FROM TeamPoints t
    JOIN PointsChange p ON t.team_id = p.team_id
)
SELECT a.team_id, a.name, CAST(b.rk AS SIGNED) - CAST(a.rk AS SIGNED) AS rank_diff
FROM aft a
JOIN bef b ON a.team_id = b.team_id
