SELECT ROUND(AVG(num), 1) AS median
FROM
    (SELECT *, SUM(frequency) OVER () total, SUM(frequency) OVER (ORDER BY num) acc
    FROM Numbers
    ) t1
WHERE acc - frequency <= total / 2 AND acc >= total / 2