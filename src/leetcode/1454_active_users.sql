SELECT DISTINCT id, name
FROM
    (SELECT DISTINCT a.id, a.name, l.login_date, DENSE_RANK() OVER (PARTITION BY a.id ORDER BY l.login_date) AS rk
    FROM Logins l
    JOIN Accounts a ON l.id = a.id) t1
GROUP BY 1, 2, login_date - INTERVAL rk day
HAVING COUNT(*) >= 5
ORDER BY id
