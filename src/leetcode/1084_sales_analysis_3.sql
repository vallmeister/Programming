SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s ON p.product_id = s.product_id
GROUP BY 1, 2
HAVING MIN(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31' AND MAX(s.sale_date) BETWEEN '2019-01-01' AND '2019-03-31'