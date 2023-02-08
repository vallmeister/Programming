SELECT customer_id
FROM (
    SELECT DISTINCT *
    FROM Customer
     ) t1
GROUP BY 1
HAVING COUNT(*) = (SELECT COUNT(*) FROM Product)
