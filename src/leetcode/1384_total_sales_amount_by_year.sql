WITH RECURSIVE t1 AS (
    SELECT product_id, period_start AS curr_day, period_start, period_end, average_daily_sales
    FROM Sales
    UNION ALL
    SELECT product_id, DATE_ADD(curr_day, INTERVAL 1 DAY), period_start, period_end, average_daily_sales
    FROM t1
    WHERE curr_day < period_end
)
SELECT p.product_id, p.product_name, LEFT(t1.curr_day, 4) AS report_year, SUM(average_daily_sales) total_amount
FROM t1
JOIN Product p
ON t1.product_id = p.product_id
GROUP BY 1, 2, 3
ORDER BY 1, 3
