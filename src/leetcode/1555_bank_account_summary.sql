SELECT user_id, user_name, credit + COALESCE(SUM(amount), 0) AS credit,
       CASE WHEN credit + COALESCE(SUM(amount), 0) < 0 THEN 'Yes' ELSE 'No' END AS credit_limit_breached
FROM (
    SELECT u.user_id, u.user_name, u.credit, - t.amount AS amount
    FROM Users u
    LEFT JOIN Transactions t ON u.user_id = t.paid_by
    UNION ALL
    SELECT u.user_id, u.user_name, u.credit, t.amount
    FROM Users u
    LEFT JOIN Transactions t ON u.user_id = t.paid_to
     ) t1
GROUP BY 1, 2
