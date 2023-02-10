WITH friends AS (
    SELECT user2_id AS user
    FROM Friendship
    WHERE user1_id = 1
    UNION
    SELECT user1_id AS user
    FROM Friendship
    WHERE user2_id = 1
)
SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE user_id IN (SELECT * FROM friends)
AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id = 1)
