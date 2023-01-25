WITH orders_2019 AS (
    SELECT *
    FROM Orders
    WHERE YEAR(order_date) = 2019
)

SELECT o1.buyer_id, u.join_date, COUNT(o1.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN orders_2019 AS o1 ON u.user_id = o1.buyer_id
GROUP BY 1, 2
ORDER BY 1
