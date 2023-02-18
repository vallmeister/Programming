SELECT airport_id
FROM
    (SELECT airport_id, SUM(flights_count) traffic, MAX(SUM(flights_count)) OVER () max_traffic
    FROM
        (SELECT departure_airport airport_id, flights_count
        FROM Flights
        UNION ALL
        SELECT arrival_airport airport_id, flights_count
        FROM Flights) t1
    GROUP BY 1) t2
WHERE traffic = max_traffic
