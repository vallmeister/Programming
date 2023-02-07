WITH first_log AS (
    SELECT player_id, MIN(event_date) first_event
    FROM Activity
    GROUP BY player_id
),
consec_players AS (
    SELECT f.player_id, f.first_event, a.event_date
    FROM first_log f
    JOIN Activity a ON f.player_id = a.player_id AND f.first_event + 1 = a.event_date
)
SELECT ROUND((SELECT COUNT(*) FROM consec_players) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
