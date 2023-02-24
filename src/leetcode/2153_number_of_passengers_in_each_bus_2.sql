WITH t1 AS (
    SELECT *, COALESCE(LAG(arrival_time) OVER (ORDER BY arrival_time), 0) prev
    FROM Buses
),
t2 AS (
    SELECT bus_id, SUM(capacity) OVER (ORDER BY arrival_time) all_capacity
    FROM Buses
),
t3 AS (
    SELECT t1.bus_id, t1.capacity, p.passenger_id, t2.all_capacity
    FROM t1
    LEFT JOIN Passengers p
    ON p.arrival_time > t1.prev
    AND p.arrival_time <= t1.arrival_time
    LEFT JOIN t2
    ON t1.bus_id = t2.bus_id
),
t4 AS (
    SELECT DISTINCT bus_id, capacity, all_capacity, COUNT(passenger_id) OVER (ORDER BY all_capacity) all_passengers
    FROM t3
)
SELECT *, COALESCE(LAG(all_passengers - all_capacity) OVER (ORDER BY all_capacity), 0) left_before
FROM t4