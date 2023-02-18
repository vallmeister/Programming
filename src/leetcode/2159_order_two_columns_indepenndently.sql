WITH t1 AS (
    SELECT first_col, ROW_NUMBER() OVER (ORDER BY first_col) AS rw
    FROM Data
),
    t2 AS (
        SELECT second_col, ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rw
        FROM Data
    )
SELECT t1.first_col, t2.second_col
FROM t1
JOIN t2 ON t1.rw = t2.rw
