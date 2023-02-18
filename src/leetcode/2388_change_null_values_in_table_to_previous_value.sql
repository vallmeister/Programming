WITH t1 AS (
    SELECT *, ROW_NUMBER() OVER () rw
    FROM CoffeeShop
)
SELECT id, CASE WHEN drink IS NOT NULL THEN drink ELSE (
    SELECT t1.drink
    FROM t1
    WHERE t1.rw < t2.rw AND t1.drink IS NOT NULL
    ORDER BY t1.rw DESC
    LIMIT 1
    ) END AS drink
FROM t1 t2
