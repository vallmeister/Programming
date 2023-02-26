WITH t1 AS (
    SELECT p1.invoice_id, p1.product_id, p1.quantity, p2.price,
           SUM(p1.quantity * p2.price) OVER (PARTITION BY p1.invoice_id) total
    FROM Purchases p1
    JOIN Products p2
    ON p1.product_id = p2.product_id
)
SELECT product_id, quantity, price
FROM (SELECT product_id, quantity, quantity * price AS price, RANK() OVER (ORDER BY total DESC, invoice_id) rk
      FROM t1) t2
WHERE rk = 1
