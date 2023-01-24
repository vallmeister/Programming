WITH t1 AS (
SELECT d.name Department, MAX(e.salary) salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
GROUP BY 1)

SELECT t1.Department, e.name Employee, t1.salary Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
JOIN t1 ON t1.Department = d.name AND t1.salary = e.salary
