WITH t1 AS (
    SELECT candidate_id, interview_id
    FROM Candidates
    WHERE years_of_exp >= 2
),
t2 AS (
    SELECT interview_id
    FROM Rounds
    GROUP BY 1
    HAVING SUM(score) > 15
)
SELECT t1.candidate_id
FROM t1
JOIN t2 ON t1.interview_id = t2.interview_id
