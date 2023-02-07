WITH unique_cities AS (
    SELECT lat, lon
    FROM Insurance
    GROUP BY 1, 2
    HAVING COUNT(*) = 1
),
same_tivs AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(tiv_2015) > 1
)
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE (lat, lon) IN (SELECT * FROM unique_cities)
AND tiv_2015 IN (SELECT * FROM same_tivs)
