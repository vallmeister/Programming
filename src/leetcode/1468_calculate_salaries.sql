SELECT company_id, employee_id, employee_name,
       CASE WHEN max_sal > 10000 THEN ROUND(salary * (1 - 0.49), 0) WHEN max_sal < 1000 THEN salary ELSE ROUND(salary * (1 - 0.24), 0) END AS salary
FROM
    (SELECT *, MAX(salary) OVER (PARTITION BY company_id) AS max_sal
    FROM Salaries) t1
