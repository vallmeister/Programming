WITH avgs AS (
    SELECT event_type, AVG(occurences) AS average
    FROM Events
    GROUP BY 1
)
SELECT e.business_id
FROM Events e
JOIN avgs a ON e.event_type = a.event_type
WHERE e.occurences > a.average
GROUP BY 1
HAVING COUNT(*) > 1

-- Alternatively with window function
SELECT business_id
FROM (SELECT *, AVG(occurences) OVER (PARTITION BY event_type) AS average
      FROM Events) t1
WHERE occurences > average
GROUP BY 1
HAVING COUNT(*) > 1
