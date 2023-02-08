WITH first_years AS (
    SELECT product_id, MIN(Sales.year) AS first_year
    FROM Sales
    GROUP BY 1
)
SELECT s.product_id, f.first_year, s.quantity, s.price
FROM Sales s
JOIN first_years f ON s.product_id = f.product_id AND f.first_year = s.year
