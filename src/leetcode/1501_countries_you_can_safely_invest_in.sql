WITH t1 AS (
    SELECT p1.name caller_name, c2.name caller_country, c1.caller_id, c1.duration, c1.callee_id, c3.name callee_country, p2.name callee_name
    FROM Calls c1
    JOIN Person p1 ON p1.id = c1.caller_id
    JOIN Person p2 ON p2.id = c1.callee_id
    JOIN Country c2 ON LEFT(p1.phone_number, 3) = c2.country_code
    JOIN Country c3 ON LEFT(p2.phone_number, 3) = c3.country_code
),
t2 AS (
    SELECT caller_country country, duration
    FROM t1
    UNION ALL
    SELECT callee_country, duration
    FROM t1
)
SELECT country
FROM t2
GROUP BY 1
HAVING AVG(duration) > (SELECT AVG(duration) FROM t2)
