WITH unique_posts AS (
    SELECT DISTINCT post_id, action_date
    FROM Actions
    WHERE extra = 'spam'
),
daily_percent AS (
    SELECT u.action_date, COUNT(r.post_id) / COUNT(*) * 100 AS daily_percent
    FROM unique_posts u
    LEFT JOIN Removals r ON u.post_id = r.post_id
    GROUP BY 1
)
SELECT ROUND(AVG(daily_percent), 2) average_daily_percent
FROM daily_percent
