SELECT player_id, player_name, SUM(grand_slams_count) grand_slams_count
FROM
    (SELECT p.player_id, p.player_name, COUNT(*) grand_slams_count
    FROM Championships c
    JOIN Players p ON p.player_id = c.Wimbledon
    GROUP BY 1
    UNION ALL
    SELECT p.player_id, p.player_name, COUNT(*) grand_slams_count
    FROM Championships c
    JOIN Players p ON p.player_id = c.Fr_open
    GROUP BY 1
    UNION ALL
    SELECT p.player_id, p.player_name, COUNT(*) grand_slams_count
    FROM Championships c
    JOIN Players p ON p.player_id = c.Us_open
    GROUP BY 1
    UNION ALL
    SELECT p.player_id, p.player_name, COUNT(*) grand_slams_count
    FROM Championships c
    JOIN Players p ON p.player_id = c.Au_open
    GROUP BY 1) t1
GROUP BY 1
