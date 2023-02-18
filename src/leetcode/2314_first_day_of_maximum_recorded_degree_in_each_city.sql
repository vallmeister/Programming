SELECT city_id, t1.day, t1.degree
FROM
    (SELECT *, RANK() OVER (PARTITION BY city_id ORDER BY Weather.degree DESC, Weather.day) rk
    FROM Weather) t1
WHERE rk = 1
