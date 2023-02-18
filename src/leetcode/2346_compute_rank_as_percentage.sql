SELECT student_id, department_id, ROUND((rk - 1) / CASE WHEN cnt = 1 THEN 1 ELSE cnt - 1 END * 100, 2) AS percentage
FROM
    (SELECT student_id, department_id,
           COUNT(*) OVER (PARTITION BY department_id) cnt,
           RANK() OVER (PARTITION BY department_id ORDER BY mark DESC) rk
    FROM Students) t1
