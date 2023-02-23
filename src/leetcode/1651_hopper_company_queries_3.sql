WITH RECURSIVE t1 AS (
    SELECT 1 AS m
    UNION ALL
    SELECT m + 1 FROM t1 WHERE m < 12
),
t2 AS (
    SELECT a.ride_id, r.requested_at, a.ride_distance, a.ride_duration
    FROM AcceptedRides a
    JOIN Rides r ON a.ride_id = r.ride_id
    WHERE year(r.requested_at) = 2020
),
t3 AS (
    SELECT t1.m, SUM(COALESCE(t2.ride_distance, 0)) dist, SUM(COALESCE(t2.ride_duration, 0)) dur
    FROM t1
    LEFT JOIN t2
    ON t1.m = month(t2.requested_at)
    GROUP BY 1
)
SELECT a.m AS 'month', ROUND((a.dist + b.dist + c.dist) / 3, 2) average_ride_distance,
       ROUND((a.dur + b.dur + c.dur) / 3, 2) average_ride_duration
FROM t3 a
LEFT JOIN t3 b
ON a.m + 1 = b.m
LEFT JOIN t3 c
ON a.m + 2 = c.m
WHERE a.m <= 10
