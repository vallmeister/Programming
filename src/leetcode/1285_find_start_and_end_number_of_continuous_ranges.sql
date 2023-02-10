WITH t1 AS (
    SELECT log_id, RANK() OVER (ORDER BY log_id) AS rk
    FROM Logs
)
SELECT MIN(log_id) start_id, MAX(log_id) end_id
FROM t1
GROUP BY log_id - rk
