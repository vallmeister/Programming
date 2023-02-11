SELECT sale_date, SUM(CASE WHEN fruit = 'apples' THEN sold_num WHEN fruit = 'oranges' THEN -sold_num ELSE 0 END) AS diff
FROM Sales
GROUP BY 1
ORDER BY 1
