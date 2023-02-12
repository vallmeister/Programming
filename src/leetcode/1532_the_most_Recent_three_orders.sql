SELECT name AS customer_name, customer_id, order_id, order_date
FROM (
    SELECT c.name, c.customer_id, o.order_id, o.order_date,
           RANK() OVER (PARTITION BY c.name, c.customer_id ORDER BY c.name, c.customer_id, o.order_date DESC) AS rk
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
     ) t1
WHERE rk <= 3
