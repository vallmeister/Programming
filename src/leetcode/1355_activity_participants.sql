SELECT activity
FROM Friends
GROUP BY 1
HAVING COUNT(*) != (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 DESC LIMIT 1)
AND COUNT(*) != (SELECT COUNT(*) FROM Friends GROUP BY activity ORDER BY 1 LIMIT 1)
