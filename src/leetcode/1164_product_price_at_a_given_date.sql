WITH t1 AS (
    SELECT product_id,
    CASE WHEN change_date > '2019-08-16' THEN 10 ELSE new_price END AS new_price,
    CASE WHEN change_date > '2019-08-16' THEN '0000-01-01' ELSE change_date END AS change_date
    FROM Products
)
SELECT DISTINCT product_id, price
FROM (SELECT product_id, new_price price, RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rk
      FROM t1
      WHERE change_date <= '2019-08-16') t2
WHERE rk = 1
