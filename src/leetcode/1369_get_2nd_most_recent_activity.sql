WITH t1 AS (
    SELECT *, RANK() OVER (PARTITION BY username ORDER BY endDate DESC) rk
    FROM UserActivity
)
SELECT t1.username, COALESCE(t2.activity, t1.activity) activity, COALESCE(t2.startDate, t1.startDate) startDate,
       COALESCE(t2.endDate, t1.endDate) endDate
FROM t1
LEFT JOIN t1 t2 ON t1.username = t2.username
AND t1.rk + 1 = t2.rk
WHERE t1.rk = 1
