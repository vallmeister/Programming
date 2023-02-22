WITH t1 AS (
    SELECT exam_id, student_id, score, MAX(score) OVER (PARTITION BY exam_id) high,
           MIN(score) OVER (PARTITION BY exam_id) low
    FROM Exam
)
SELECT DISTINCT s.student_id, student_name
FROM Student s
JOIN Exam e ON s.student_id = e.student_id
WHERE e.student_id NOT IN (SELECT student_id
                            FROM t1
                            WHERE score = high
                            OR score = low)
ORDER BY 1
