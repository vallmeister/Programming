SELECT id, company, salary
FROM
    (SELECT *, DENSE_RANK() OVER (PARTITION BY company ORDER BY salary, id) rk, COUNT(*) OVER (PARTITION BY company) cnt
    FROM Employee) t1
WHERE CASE WHEN cnt % 2 = 0 THEN rk = cnt / 2 OR rk = cnt / 2 + 1 ELSE rk = (cnt + 1) / 2 END

-- without built-in / window-function
WITH t1 AS
    (SELECT e1.*, COUNT(*) rk
    FROM Employee e1, Employee e2
    WHERE e1.company = e2.company
    AND (e1.salary > e2.salary OR e1.salary = e2.salary AND e1.id >= e2.id)
    GROUP BY e1.id, e1.company, e1.salary
    ORDER BY e1.company, e1.salary, e1.id, e2.salary, e2.id),
t2 AS
    (SELECT company, MAX(rk) num
    FROM t1
    GROUP BY 1)
SELECT t1.id, t1.company, t1.salary
FROM t1
JOIN t2 ON t1.company = t2.company
WHERE CASE WHEN num % 2 = 0 THEN rk = num / 2 OR rk = num / 2 + 1 ELSE rk = (num + 1) / 2 END
