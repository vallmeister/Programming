WITH t1 AS (
    SELECT 'desktop' AS platform
    UNION
    SELECT 'mobile' AS platform
    UNION
    SELECT 'both' AS platform
),
t2 AS (
    SELECT DISTINCT spend_date
    FROM Spending
),
t3 AS
    (SELECT user_id, spend_date, platform, amount
    FROM Spending
    WHERE platform = 'desktop'
    AND (user_id, spend_date, 'mobile') NOT IN (SELECT user_id, spend_date, platform FROM Spending)
    UNION ALL
    SELECT user_id, spend_date, platform, amount
    FROM Spending
    WHERE platform = 'mobile'
    AND (user_id, spend_date, 'desktop') NOT IN (SELECT user_id, spend_date, platform FROM Spending)
    UNION ALL
    SELECT user_id, spend_date, 'both' AS platform, amount
    FROM Spending
    WHERE (user_id, spend_date, 'desktop') IN (SELECT user_id, spend_date, platform FROM Spending)
    AND (user_id, spend_date, 'mobile') IN (SELECT user_id, spend_date, platform FROM Spending))
SELECT t2.spend_date, t1.platform, SUM(COALESCE(t3.amount, 0)) total_amount, COUNT(DISTINCT t3.user_id) total_users
FROM t2 CROSS JOIN t1
LEFT JOIN t3 ON t2.spend_date = t3.spend_date AND t1.platform = t3.platform
GROUP BY 1, 2
