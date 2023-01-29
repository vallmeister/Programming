WITH t1 AS (
    SELECT t.id, t.client_id, u1.banned ban_c, u1.role r1, t.driver_id, u2.banned ban_d, u2.role r2, t.status, t.request_at
    FROM Trips t
    LEFT JOIN Users u1 ON t.client_id = u1.users_id
    LEFT JOIN Users u2 ON t.driver_id = u2.users_id
    WHERE u1.banned = 'No' AND u2.banned = 'No'
    ORDER BY 1),
count_cancellations AS (
    SELECT request_at, COUNT(*) cancelled
    FROM t1
    WHERE status LIKE 'cancelled%'
    GROUP BY request_at
),
count_total AS (
    SELECT request_at, COUNT(*) total
    FROM t1
    GROUP BY request_at
)
SELECT DISTINCT t1.request_at AS 'Day', IFNULL(ROUND(c1.cancelled / c2.total, 2), 0) AS 'Cancellation Rate'
FROM t1
LEFT JOIN count_cancellations c1 ON t1.request_at = c1.request_at
LEFT JOIN count_total c2 ON t1.request_at = c2.request_at
WHERE t1.request_at BETWEEN "2013-10-01" AND "2013-10-03"
ORDER BY 1
