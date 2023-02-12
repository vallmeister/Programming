SELECT product_name, product_id, order_id, order_date
FROM (
    SELECT p.product_name, p.product_id, o.order_id, o.order_date,
           RANK() OVER (PARTITION BY p.product_name ORDER BY o.order_date DESC) AS rk
    FROM Products p
    JOIN Orders o ON o.product_id = p.product_id
     ) t1
WHERE rk = 1
ORDER BY 1, 2, 3
