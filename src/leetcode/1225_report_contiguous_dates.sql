SELECT period_state, MIN(dt) start_date, MAX(dt) end_date
FROM
    (SELECT 'failed' AS period_state, fail_date AS dt, RANK() OVER (ORDER BY fail_date) rk
    FROM Failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT 'succeeded' AS period_state, success_date as dt, RANK() OVER (ORDER BY success_date) rk
    FROM Succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31') t1
GROUP BY period_state, dayofyear(dt) - rk
ORDER BY 2
