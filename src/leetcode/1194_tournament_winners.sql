SELECT GROUP_ID, PLAYER_ID
FROM
    (SELECT p.group_id GROUP_ID, t1.player_id PLAYER_ID,
           RANK() OVER(PARTITION BY p.group_id ORDER BY SUM(t1.score) DESC, t1.player_id) rk
    FROM
        (SELECT first_player AS player_id, first_score AS score
        FROM Matches
        UNION ALL
        SELECT second_player, second_score
        FROM Matches) t1
    JOIN Players p ON t1.player_id = p.player_id
    GROUP BY 1, 2) t2
WHERE rk = 1
