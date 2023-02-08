WITH most_experienced AS (
    SELECT p.project_id, MAX(e.experience_years)
    FROM Project p
    JOIN Employee e ON p.employee_id = e.employee_id
    GROUP BY 1
)
SELECT p.project_id, p.employee_id
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
WHERE (p.project_id, e.experience_years) IN (SELECT * FROM most_experienced)
