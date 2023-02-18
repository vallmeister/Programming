WITH drivers AS (
    SELECT DISTINCT driver_id
    FROM Rides
)
SELECT d.driver_id, COUNT(r.ride_id) cnt
FROM drivers d
LEFT JOIN Rides r
ON r.passenger_id = d.driver_id
GROUP BY 1
