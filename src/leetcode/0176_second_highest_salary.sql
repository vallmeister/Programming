WITH t1 AS (
    SELECT DISTINCT salary AS SecondHighestSalary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1)
SELECT CASE WHEN COUNT(*) < 1 THEN NULL ELSE (SELECT * FROM t1) END AS SecondHighestSalary
FROM t1
