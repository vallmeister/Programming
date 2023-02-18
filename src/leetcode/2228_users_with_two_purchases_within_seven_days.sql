SELECT DISTINCT user_id
FROM
    (SELECT p1.user_id
    FROM Purchases p1
    JOIN Purchases p2
    ON p1.purchase_id != p2.purchase_id
    AND p1.user_id = p2.user_id
    AND DATEDIFF(p1.purchase_date, p2.purchase_date) BETWEEN 0 AND 7) t1
ORDER BY 1
