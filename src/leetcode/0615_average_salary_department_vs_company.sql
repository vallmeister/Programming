SELECT DISTINCT pay_month, department_id,
       CASE WHEN avg_dept > avg_comp THEN 'higher' WHEN avg_dept = avg_comp THEN 'same' ELSE 'lower' END AS comparison
FROM
    (SELECT DATE_FORMAT(s.pay_date, '%Y-%m') pay_month, e.department_id,
           AVG(s.amount) OVER (PARTITION BY e.department_id, DATE_FORMAT(s.pay_date, '%Y-%m')) avg_dept,
            AVG(s.amount) OVER (PARTITION BY DATE_FORMAT(s.pay_date, '%Y-%m')) avg_comp
    FROM Salary s
    JOIN Employee e
    ON e.employee_id = s.employee_id) t1
