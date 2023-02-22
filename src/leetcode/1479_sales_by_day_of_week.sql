WITH t1 AS
    (SELECT i.item_category cat, DATE_FORMAT(o.order_date, '%W') dow, SUM(o.quantity) amt
    FROM Orders o
    JOIN Items i ON o.item_id = i.item_id
    GROUP BY 1, 2
    ORDER BY 1, 2),
t2 AS (
    SELECT DISTINCT item_category AS CATEGORY
    FROM Items
),
t3 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Monday'
),
t4 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Tuesday'
),
t5 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Wednesday'
),
t6 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Thursday'
),
t7 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Friday'
),
t8 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Saturday'
),
t9 AS (
    SELECT cat, amt FROM t1 WHERE dow = 'Sunday'
)
SELECT t2.CATEGORY, COALESCE(t3.amt, 0) MONDAY, COALESCE(t4.amt, 0) TUESDAY, COALESCE(t5.amt, 0) WEDNESDAY,
    COALESCE(t6.amt, 0) THURSDAY, COALESCE(t7.amt, 0) FRIDAY, COALESCE(t8.amt, 0) SATURDAY,
    COALESCE(t9.amt, 0) SUNDAY
FROM t2
LEFT JOIN t3 ON t2.CATEGORY = t3.cat
LEFT JOIN t4 ON t2.CATEGORY = t4.cat
LEFT JOIN t5 ON t2.CATEGORY = t5.cat
LEFT JOIN t6 ON t2.CATEGORY = t6.cat
LEFT JOIN t7 ON t2.CATEGORY = t7.cat
LEFT JOIN t8 ON t2.CATEGORY = t8.cat
LEFT JOIN t9 ON t2.CATEGORY = t9.cat
ORDER BY 1
