SELECT SUM(CASE WHEN weekday(submit_date) BETWEEN 5 AND 6 THEN 1 ELSE 0 END) AS weekend_cnt,
       SUM(CASE WHEN weekday(submit_date) BETWEEN 0 AND 4 THEN 1 ELSE 0 END) AS working_cnt
FROM Tasks