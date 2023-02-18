WITH t1 AS (SELECT *, COALESCE(LAG(arrival_time) OVER(ORDER BY arrival_time), 0) AS prev_time
            FROM Buses)
SELECT bus_id, COUNT(passenger_id) passengers_cnt
FROM t1
LEFT JOIN Passengers p
ON p.arrival_time <= t1.arrival_time
AND p.arrival_time > t1.prev_time
GROUP BY 1
ORDER BY 1
