WITH t1 AS (
    SELECT user_id, gender, RANK() OVER (ORDER BY user_id) AS rk
    FROM Genders
    WHERE gender = 'female'
),
t2 AS (
    SELECT user_id, gender, RANK() OVER (ORDER BY user_id) AS rk
    FROM Genders
    WHERE gender = 'other'
),
t3 AS (
    SELECT user_id, gender, RANK() OVER (ORDER BY user_id) AS rk
    FROM Genders
    WHERE gender = 'male'
)
SELECT user_id, gender
FROM
    (SELECT user_id, gender, rk
    FROM t1
    UNION ALL
    SELECT user_id, gender, rk
    FROM t2
    UNION ALL
    SELECT user_id, gender, rk
    FROM t3
    ORDER BY rk, CASE WHEN gender = 'female' THEN 0 WHEN gender = 'other' THEN 1 ELSE 2 END) t4
