WITH gold AS (
    SELECT gold_medal
    FROM Contests
    GROUP BY 1
    HAVING COUNT(*) >= 3
),
any AS (
    SELECT c.contest_id, u.user_id, u.mail, u.name, RANK() OVER (PARTITION BY u.user_id ORDER BY c.contest_id) as rk
    FROM Contests c
    JOIN Users u ON c.gold_medal = u.user_id
    OR c.silver_medal = u.user_id
    OR c.bronze_medal = u.user_id
)
SELECT DISTINCT name, mail
FROM Users
WHERE user_id IN (SELECT * FROM gold)
OR user_id IN (
    SELECT user_id
    FROM any
    GROUP BY user_id, contest_id - rk
    HAVING COUNT(*) >= 3
    )
