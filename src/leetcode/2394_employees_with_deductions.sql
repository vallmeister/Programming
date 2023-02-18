SELECT DISTINCT employee_id
FROM
    (SELECT e.employee_id, e.needed_hours * 60 needed,
           SUM(COALESCE(CEIL(TIMESTAMPDIFF(second, l.in_time, l.out_time) / 60), 0)) OVER (PARTITION BY e.employee_id, DATE_FORMAT(l.in_time, '%Y-%m')) worked
    FROM Employees e
    LEFT JOIN Logs l ON e.employee_id = l.employee_id) t1
WHERE needed > worked
