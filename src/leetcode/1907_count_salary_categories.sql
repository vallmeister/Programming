WITH t1 AS (
    SELECT *,
       CASE WHEN income < 20000 THEN 'Low Salary' WHEN income > 50000 THEN 'High Salary' ELSE 'Average Salary' END AS category
    FROM Accounts
),
t2 AS (
    SELECT 'High Salary' AS category
    UNION
    SELECT 'Average Salary' AS category
    UNION
    SELECT 'Low Salary' AS category
)
SELECT t2.category, COUNT(t1.account_id) accounts_count
FROM t2
LEFT JOIN t1 ON t2.category = t1.category
GROUP BY 1
