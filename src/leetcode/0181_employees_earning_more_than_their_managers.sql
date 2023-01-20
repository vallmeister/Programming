SELECT employee Employee FROM
(SELECT a.id, a.name employee, a.salary emp_salary, a.managerId, b.name manager, b.salary manager_salary
FROM employee a
JOIN employee b ON a.managerId = b.id
WHERE a.salary > b.salary) t1