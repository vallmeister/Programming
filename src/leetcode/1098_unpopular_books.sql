WITH t1 AS (
    SELECT book_id, name
    FROM Books
    WHERE available_from <= '2019-06-23' - INTERVAL 1 month
),
t2 AS (
    SELECT book_id, quantity
    FROM Orders
    WHERE dispatch_date >= '2019-06-23' - INTERVAL 1 year
    )
SELECT t1.book_id, t1.name
FROM t1
LEFT JOIN t2 ON t2.book_id = t1.book_id
GROUP BY 1, 2
HAVING SUM(COALESCE(t2.quantity, 0)) < 10
