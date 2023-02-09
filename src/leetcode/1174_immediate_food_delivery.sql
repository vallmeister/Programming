WITH fst AS (
    SELECT customer_id, MIN(order_date) AS fst
    FROM Delivery
    GROUP BY 1
)
SELECT ROUND((SELECT COUNT(*) FROM Delivery WHERE (customer_id, customer_pref_delivery_date) IN (SELECT * FROM fst)) /
       (SELECT COUNT(*) FROM fst) * 100, 2) AS immediate_percentage