WITH t1 AS
    (SELECT u.user_id, u.favorite_brand, o.order_date, i.item_brand,
           RANK() OVER (PARTITION BY u.user_id ORDER BY o.order_date) rk
    FROM Users u
    LEFT JOIN Orders o ON u.user_id = o.seller_id
    LEFT JOIN Items i ON o.item_id = i.item_id),
t2 AS (
    SELECT user_id seller_id,
       CASE WHEN rk = 2 AND favorite_brand = item_brand THEN 'yes' ELSE 'no' END AS '2nd_item_fav_brand'
    FROM t1)
SELECT DISTINCT *
FROM t2
WHERE 2nd_item_fav_brand = 'yes'
UNION
SELECT DISTINCT *
FROM t2
WHERE (seller_id) NOT IN (SELECT seller_id FROM t2 WHERE 2nd_item_fav_brand = 'yes')
