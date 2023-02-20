WITH t1 AS (
    SELECT DISTINCT player_id, MIN(event_date) install_dt
    FROM Activity
    GROUP BY player_id
)
SELECT t1.install_dt, COUNT(DISTINCT a1.player_id) AS installs,
       ROUND(COUNT(DISTINCT a2.player_id) / COUNT(DISTINCT a1.player_id), 2) AS Day1_retention
FROM t1
LEFT JOIN Activity a1 ON t1.install_dt = a1.event_date AND t1.player_id = a1.player_id
LEFT JOIN Activity a2 ON DATE_ADD(t1.install_dt, INTERVAL 1 day) = a2.event_date
AND a1.player_id = a2.player_id
GROUP BY t1.install_dt
