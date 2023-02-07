SELECT e2.name
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
GROUP BY 1
HAVING COUNT(*) >= 5
ORDER BY 1
