SELECT id, COUNT(*) num
FROM
    (SELECT requester_id id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id id
    FROM RequestAccepted) t1
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1
