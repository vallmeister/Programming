WITH RECURSIVE t1 AS (
    SELECT 1 AS m
    UNION ALL
    SELECT m + 1 FROM t1 WHERE m < 12
),
t2 AS (
    SELECT driver_id, join_date, COUNT(*) OVER (ORDER BY DATE_FORMAT(join_date, '%Y-%m')) active_drivers
    FROM Drivers
),
t3 AS (
    SELECT driver_id, join_date, active_drivers
    FROM t2
    WHERE year(join_date) = 2020
),
t4 AS (
    SELECT DISTINCT t1.m, t3.active_drivers
    FROM t1
    LEFT JOIN t3
    ON t1.m = month(t3.join_date)
    ),
t5 AS (
    SELECT t4.m, COALESCE(t4.active_drivers, (
        SELECT MAX(cte.active_drivers)
        FROM t4 cte
        WHERE t4.m > cte.m AND cte.active_drivers IS NOT NULL
    ), 0) AS active_drivers
    FROM t4
),
t6 AS (
    SELECT a.ride_id, r.requested_at
    FROM Rides r
    JOIN AcceptedRides a
    ON r.ride_id = a.ride_id
    AND year(r.requested_at) = 2020
)
SELECT t5.m AS 'month', t5.active_drivers, COUNT(t6.ride_id) accepted_rides
FROM t5
LEFT JOIN t6
ON month(t6.requested_at) = t5.m
GROUP BY 1, 2
