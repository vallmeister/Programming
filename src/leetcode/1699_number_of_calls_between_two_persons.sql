SELECT from_id person1, to_id person2, COUNT(*) call_count, SUM(duration) total_duration
FROM
    (SELECT from_id, to_id, duration
    FROM Calls
    UNION ALL
    SELECT to_id, from_id, duration
    FROM Calls) t1
WHERE from_id < to_id
GROUP BY 1, 2
