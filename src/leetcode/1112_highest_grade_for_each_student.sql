WITH t1 AS (
    SELECT *, RANK() OVER (PARTITION BY student_id ORDER BY grade DESC, course_id) AS rk
    FROM Enrollments
)
SELECT student_id, course_id, grade
FROM t1
WHERE rk = 1
ORDER BY 1
