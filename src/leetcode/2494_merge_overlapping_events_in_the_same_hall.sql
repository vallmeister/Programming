WITH t2 AS (
    SELECT hall_id, start_day, end_day, COALESCE(LAG(mx) OVER (PARTITION BY hall_id ORDER BY start_day), '0001-01-01') lst
    FROM
        (SELECT *, MAX(end_day) OVER (PARTITION BY hall_id ORDER BY start_day) mx
        FROM HallEvents) t1
)
SELECT hall_id, MIN(start_day) start_day, MAX(end_day) end_day
FROM
    (SELECT *, SUM(CASE WHEN start_day > lst THEN 1 ELSE 0 END) OVER (PARTITION BY hall_id ORDER BY start_day) grp
    FROM t2) t3
GROUP BY hall_id, grp
