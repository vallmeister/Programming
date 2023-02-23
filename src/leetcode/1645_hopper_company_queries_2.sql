WITH RECURSIVE t1 AS (
    SELECT 1 AS m
    UNION ALL
    SELECT m + 1 FROM t1 WHERE m < 12
),
t2 AS (
    SELECT CASE WHEN year(join_date) < 2020 THEN 1 ELSE month(join_date) END AS mon, driver_id
    FROM Drivers
    WHERE year(join_date) <= 2020
),
t3 AS (
    SELECT DISTINCT t1.m, COUNT(t2.driver_id) OVER (ORDER BY t1.m) AS available_drivers
    FROM t1
    LEFT JOIN t2
    ON t1.m = t2.mon
),
t4 AS (
    SELECT a.ride_id, r.requested_at, a.driver_id
    FROM AcceptedRides a
    JOIN Rides r
    ON a.ride_id = r.ride_id
    WHERE year(r.requested_at) = 2020
)
SELECT t3.m AS 'month',
    COALESCE(ROUND(COUNT(DISTINCT t4.driver_id) / t3.available_drivers * 100, 2), 0) AS working_percentage
FROM t3
LEFT JOIN t4
ON t3.m = month(t4.requested_at)
GROUP BY 1
