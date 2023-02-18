WITH t1 AS
    (SELECT a.account_id, a.max_income, DATE_FORMAT(t.day, '%Y-%m') mon, SUM(t.amount) income
    FROM Accounts a
    JOIN Transactions t ON a.account_id = t.account_id AND t.type = 'Creditor'
    GROUP BY 1, 2, 3
    ORDER BY 1, 3)
SELECT DISTINCT t1.account_id
FROM t1
JOIN t1 t2 ON t1.account_id = t2.account_id
AND t1.max_income < t1.income
AND t2.max_income < t2.income
AND CAST(LEFT(t1.mon, 4) AS SIGNED) * 12 + CAST(RIGHT(t1.mon, 2) AS SIGNED) + 1
        = CAST(LEFT(t2.mon, 4) AS SIGNED) * 12 + CAST(RIGHT(t2.mon, 2) AS SIGNED)
