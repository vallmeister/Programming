WITH t2 AS (
    SELECT visited_on, COUNT(*) cnt
    FROM Customer
    GROUP BY 1
),
t1 AS(
    SELECT c1.visited_on, c2.amount, t2.cnt
    FROM Customer c1
    JOIN Customer c2 ON DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
    JOIN t2 ON c1.visited_on = t2.visited_on
)
SELECT visited_on, SUM(amount) / cnt amount, ROUND(SUM(amount) / 7 / cnt, 2) average_amount
FROM t1
GROUP BY 1
ORDER BY 1
LIMIT 18446744073709551610
OFFSET 6
