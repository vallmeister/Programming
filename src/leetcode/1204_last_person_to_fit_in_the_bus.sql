SELECT person_name
FROM
    (SELECT turn, person_id, person_name, weight,
           SUM(weight) OVER(ORDER BY turn) AS total
    FROM Queue) t1
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1
