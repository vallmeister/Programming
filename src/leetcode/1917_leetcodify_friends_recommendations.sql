WITH t1 AS
    (SELECT DISTINCT l1.user_id, l2.user_id AS recommended_id
    FROM Listens l1
    JOIN Listens l2
    ON l1.user_id < l2.user_id
    AND l1.song_id = l2.song_id
    AND l1.day = l2.day
    LEFT JOIN Friendship f
    ON l1.user_id = f.user1_id AND l2.user_id = f.user2_id
    WHERE f.user1_id IS NULL
    GROUP BY 1, 2, l1.day
    HAVING COUNT(DISTINCT l1.song_id) >= 3
    ORDER BY 1, 2)
SELECT user_id, recommended_id
FROM t1
UNION
SELECT recommended_id, user_id
FROM t1
