SELECT user_id, product_id
FROM
    (SELECT s.user_id, s.product_id, RANK() OVER (PARTITION BY s.user_id ORDER BY SUM(s.quantity * p.price) DESC) rk
    FROM Sales s
    JOIN Product p ON s.product_id = p.product_id
    GROUP BY 1, 2) t1
WHERE rk = 1
ORDER BY 1, 2
