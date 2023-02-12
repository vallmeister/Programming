SELECT customer_id, product_id, product_name
FROM
    (SELECT customer_id, product_id, product_name,
           RANK() OVER (PARTITION BY customer_id ORDER BY cnt DESC) AS rk
    FROM (
        SELECT c.customer_id, p.product_id, p.product_name,
               COUNT(*) AS cnt
        FROM Orders o
        JOIN Customers c ON o.customer_id = c.customer_id
        JOIN Products p ON o.product_id = p.product_id
        GROUP BY 1, 2, 3
         ) t1) t2
WHERE rk = 1
