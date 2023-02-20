WITH t1 AS (
    SELECT *, MAX(Employee.month) OVER (PARTITION BY id) most_recent
    FROM Employee
)
SELECT t1.id, t1.month, t1.salary + COALESCE(t2.salary, 0) + COALESCE(t3.salary, 0) salary
FROM t1
LEFT JOIN t1 t2
ON t1.id = t2.id
AND t1.month = t2.month + 1
LEFT JOIN t1 t3
ON t1.id = t3.id
AND t1.month = t3.month + 2
WHERE t1.month != t1.most_recent
ORDER BY t1.id, t1.month DESC
