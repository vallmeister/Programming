SELECT DISTINCT c.customer_id, c.customer_name
FROM Customers c
JOIN Orders o ON o.customer_id = c.customer_id
WHERE (c.customer_id, 'A') IN (SELECT customer_id, product_name FROM Orders)
AND (c.customer_id, 'B') IN (SELECT customer_id, product_name FROM Orders)
AND (c.customer_id, 'C') NOT IN (SELECT customer_id, product_name FROM Orders)
