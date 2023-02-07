WITH t1 AS (
    SELECT c.name, COUNT(*) votes
    FROM Candidate c
    JOIN Vote v ON c.id = v.candidateId
    GROUP BY 1
    ORDER BY 2 DESC
)
SELECT name
FROM t1
WHERE votes = (SELECT MAX(votes) FROM t1);

-- alternative
SELECT name
FROM t1
LIMIT 1
