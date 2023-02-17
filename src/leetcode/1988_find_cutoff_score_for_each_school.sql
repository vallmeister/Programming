SELECT s.school_id, MIN(COALESCE(e.score, -1)) score
FROM Schools s
LEFT JOIN Exam e
ON s.capacity >= e.student_count
GROUP BY 1
ORDER BY s.school_id
