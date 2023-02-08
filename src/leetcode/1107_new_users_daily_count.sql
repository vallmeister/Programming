WITH first_login AS (
    SELECT user_id, MIN(activity_date) first_login
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY user_id
    HAVING MIN(activity_date) >= '2019-06-30' - INTERVAL 90 day
)
SELECT first_login AS login_date, COUNT(*) AS user_count
FROM first_login
GROUP BY 1
