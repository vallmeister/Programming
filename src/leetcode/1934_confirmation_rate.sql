SELECT s.user_id,
       ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) /
       CASE WHEN COUNT(c.action) > 0 THEN COUNT(c.action) ELSE 1 END, 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY 1
