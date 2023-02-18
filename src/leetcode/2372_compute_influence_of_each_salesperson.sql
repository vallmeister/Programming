SELECT s1.salesperson_id, s1.name, SUM(COALESCE(s2.price,0)) total
FROM Salesperson s1
LEFT JOIN Customer c ON s1.salesperson_id = c.salesperson_id
LEFT JOIN Sales s2 ON s2.customer_id = c.customer_id
GROUP BY 1, 2
ORDER BY 3 DESC
