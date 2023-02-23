WITH t1 AS (
    SELECT employee_id, experience, salary, 70000 - SUM(salary) OVER (ORDER BY salary, employee_id) budget
    FROM Candidates
    WHERE experience = 'Senior'
),
t2 AS (
    SELECT *
    FROM t1
    WHERE budget >= 0
    UNION ALL
    SELECT employee_id, experience, salary,
           (SELECT CASE WHEN (SELECT MAX(budget) FROM t1) < 0 THEN 70000
               ELSE (SELECT MIN(budget) FROM t1 WHERE budget >= 0) END)
               - SUM(salary) OVER (ORDER BY salary, employee_id) budget
    FROM Candidates
    WHERE experience = 'Junior'
),
t3 AS (
    SELECT DISTINCT experience
    FROM Candidates
)
SELECT t3.experience, COUNT(t2.employee_id) accepted_candidates
FROM t3
LEFT JOIN t2
ON t2.experience = t3.experience
AND t2.budget >= 0
GROUP BY 1
