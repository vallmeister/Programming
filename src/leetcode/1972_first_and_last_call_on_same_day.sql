WITH t1 AS (
    SELECT caller_id, recipient_id, call_time
    FROM Calls
    UNION ALL
    SELECT recipient_id, caller_id, call_time
    FROM Calls
),
t2 AS (
    SELECT *, RANK() OVER (PARTITION BY caller_id, DATE_FORMAT(call_time, '%Y-%m-%d') ORDER BY call_time) rk
    FROM t1
),
t3 AS (
    SELECT caller_id, recipient_id, call_time, rk,
           MAX(rk) OVER (PARTITION BY caller_id, DATE_FORMAT(call_time, '%Y-%m-%d')) lst
    FROM t2
)
SELECT DISTINCT a.caller_id user_id
FROM t3 a
JOIN t3 b
ON a.caller_id = b.caller_id
AND a.rk = 1
AND a.lst = b.rk
AND DATE_FORMAT(a.call_time, '%Y-%m-%d') = DATE_FORMAT(b.call_time, '%Y-%m-%d')
AND a.recipient_id = b.recipient_id
