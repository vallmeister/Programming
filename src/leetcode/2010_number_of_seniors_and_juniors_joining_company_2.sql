WITH t1 AS (SELECT *, SUM(salary) OVER (PARTITION BY experience ORDER BY salary) costs
            FROM Candidates)
SELECT employee_id
FROM t1
WHERE experience = 'Senior'
AND costs <= 70000
UNION
SELECT employee_id
FROM t1
WHERE experience = 'Junior'
AND costs <= 70000 - COALESCE((SELECT MAX(costs) FROM t1 WHERE experience = 'Senior' AND costs <= 70000), 0)
