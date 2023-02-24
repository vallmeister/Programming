WITH t1 AS (
    SELECT power,
           CONCAT(CASE WHEN factor >= 0 THEN CONCAT('+', factor) ELSE factor END,
               CASE WHEN power > 1 THEN CONCAT('X^', power) WHEN power = 1 THEN 'X' ELSE '' END) AS term
    FROM Terms
)
SELECT CONCAT(GROUP_CONCAT(term ORDER BY power DESC SEPARATOR ''), '=0') AS equation
FROM t1