WITH t1 AS (
    SELECT user1_id AS user_id, user2_id AS friend
    FROM Friendship
    UNION
    SELECT user2_id AS user_id, user1_id AS friend
    FROM Friendship
)
SELECT t1.user_id, l1.page_id, COUNT(t1.friend) friends_likes
FROM t1
JOIN Likes l1
ON t1.friend = l1.user_id
LEFT JOIN Likes l2
ON t1.user_id = l2.user_id
AND l1.page_id = l2.page_id
WHERE l2.user_id IS NULL
GROUP BY 1, 2
