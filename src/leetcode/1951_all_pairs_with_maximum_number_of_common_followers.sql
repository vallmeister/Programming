SELECT user1_id, user2_id
FROM
    (SELECT r1.user_id user1_id, r2.user_id user2_id, COUNT(*) followers,
           MAX(COUNT(*)) OVER () max_common_followers
    FROM Relations r1
    JOIN Relations r2
    ON r1.follower_id = r2.follower_id
    AND r1.user_id < r2.user_id
    GROUP BY 1, 2
    ORDER BY 1, 2) t1
WHERE followers = max_common_followers
