WITH RECURSIVE t1 AS (
    SELECT MIN(year(order_date)) AS y
    FROM Orders
    UNION ALL
    SELECT y + 1 FROM t1 WHERE y < (SELECT MAX(year(order_date)) FROM Orders)
),
t2 AS (
    SELECT customer_id, year(order_date) y, SUM(price) total_purchases
    FROM Orders
    GROUP BY 1, 2
),
t3 AS (
    SELECT customer_id, MIN(year(order_date)) fst, MAX(year(order_date)) lst
    FROM Orders
    GROUP BY 1
),
t4 AS (
    SELECT t1.y, t3.customer_id, COALESCE(t2.total_purchases, 0) total,
           COALESCE(LAG(t2.total_purchases) OVER (PARTITION BY t3.customer_id ORDER BY t1.y), 0) total_before
    FROM t1
    LEFT JOIN t3
    ON t1.y >= t3.fst
    AND t1.y <= t3.lst
    LEFT JOIN t2
    ON t1.y = t2.y
    AND t3.customer_id = t2.customer_id
),
t5 AS (
    SELECT customer_id, COUNT(customer_id) cnt, SUM(CASE WHEN total > total_before THEN 1 ELSE 0 END) strictly_greater
    FROM t4
    GROUP BY 1
)
SELECT customer_id
FROM t5
WHERE cnt = strictly_greater
