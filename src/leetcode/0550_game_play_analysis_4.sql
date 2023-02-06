WITH total_players AS (
    SELECT COUNT(DISTINCT player_id)
    FROM Activity),

consec AS (SELECT a1.player_id, a1.event_date d1, a2.event_date d2
FROM Activity a1
JOIN Activity a2 ON a1.player_id = a2.player_id AND a1.event_date + 1 = a2.event_date AND a1.games_played > 0)

SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT * FROM total_players), 2) AS fraction
FROM consec
