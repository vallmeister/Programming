WITH t2 AS (
    SELECT DATE_FORMAT(c.trans_date, '%Y-%m') AS 'month', t.country,
           COUNT(*) AS chargeback_count,
           SUM(t.amount) AS chargeback_amount
    FROM Chargebacks c
    JOIN Transactions t ON c.trans_id = t.id
    GROUP BY 1, 2
),
t1 AS (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS 'month', country,
           SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
           SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_amount
    FROM Transactions
    GROUP BY 1, 2
    HAVING SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) > 0
)
SELECT t1.month, t1.country, t1.approved_count, t1.approved_amount,
       COALESCE(t2.chargeback_count, 0) AS chargeback_count,
       COALESCE(t2.chargeback_amount, 0) AS chargeback_amount
FROM t1
LEFT JOIN t2 ON t1.month = t2.month AND t1.country = t2.country
UNION
SELECT t2.month, t2.country,
       COALESCE(t1.approved_count, 0) AS approved_count,
       COALESCE(t1.approved_amount, 0) AS approved_amount,
       t2.chargeback_count, t2.chargeback_amount
FROM t1
RIGHT JOIN t2 ON t1.month = t2.month AND t1.country = t2.country
ORDER BY 1
