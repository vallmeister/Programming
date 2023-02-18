WITH t1 AS (
    SELECT product_id, year(purchase_date) yr
    FROM ORDERS
    GROUP BY 1, 2
    HAVING COUNT(*) >= 3
    ORDER BY 1, 2
)
SELECT DISTINCT t1.product_id
FROM t1
JOIN t1 t2
ON t1.product_id = t2.product_id
AND t1.yr + 1 = t2.yr
