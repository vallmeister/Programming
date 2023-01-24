WITH t1 AS (
    SELECT d1.name, e1.salary
    FROM Employee e1
    JOIN Department d1 ON e1.departmentId = d1.id
    ORDER BY 1, 2 DESC
)

SELECT d.name, e.name, e.salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary IN (
    SELECT salary
    FROM t1
    WHERE t1.id = d.id
    LIMIT 3
    )
ORDER BY 1, 3 DESC;

-- solution
SELECT d.name Department, e.name Employee, e.salary Salary
FROM Department d
JOIN Employee e ON d.id = e.departmentId
WHERE 3 > (
    SELECT COUNT(DISTINCT e1.salary)
    FROM Employee e1
    WHERE e.salary < e1.salary AND e.departmentId = e1.departmentId
    )