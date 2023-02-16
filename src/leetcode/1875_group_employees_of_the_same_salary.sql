SELECT *, DENSE_RANK() OVER (ORDER BY salary) team_id
FROM Employees
WHERE salary IN (SELECT salary FROM Employees GROUP BY 1 HAVING COUNT(*) >= 2)
ORDER BY team_id, employee_id
