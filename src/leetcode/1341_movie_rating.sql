(SELECT u.name results
FROM Movies m1
JOIN MovieRating m2 ON m1.movie_id = m2.movie_id
JOIN Users u ON m2.user_id = u.user_id
GROUP BY 1
ORDER BY COUNT(*) DESC, 1
LIMIT 1)
UNION ALL
(SELECT m1.title results
FROM Movies m1
JOIN MovieRating m2 ON m1.movie_id = m2.movie_id
JOIN Users u ON m2.user_id = u.user_id
WHERE m2.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY 1
ORDER BY AVG(m2.rating) DESC, 1
LIMIT 1)
