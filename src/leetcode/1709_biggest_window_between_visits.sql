SELECT DISTINCT user_id, day_window as biggest_window
FROM
    (SELECT user_id, DATEDIFF(COALESCE(next_visit, '2021-01-01'), visit_date) AS day_window,
           RANK() OVER (PARTITION BY user_id ORDER BY DATEDIFF(COALESCE(next_visit, '2021-01-01'), visit_date) DESC) AS rk
    FROM
        (SELECT DISTINCT user_id, visit_date, LEAD(visit_date) OVER (PARTITION BY user_id ORDER BY visit_date) AS next_visit
        FROM UserVisits
        ORDER BY 1, 2) t1) t2
WHERE rk = 1
