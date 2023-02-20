WITH america AS (
    SELECT name AS America, ROW_NUMBER() OVER (ORDER BY name) rw
    FROM Student
    WHERE continent = 'America'
),
eu AS (
    SELECT name AS Europe, ROW_NUMBER() OVER (ORDER BY name) rw
    FROM Student
    WHERE continent = 'Europe'
),
asia AS (
    SELECT name AS Asia, ROW_NUMBER() OVER (ORDER BY name) rw
    FROM Student
    WHERE continent = 'Asia'
)
SELECT a1.America, a2.Asia, eu.Europe
FROM america a1
LEFT JOIN asia a2 ON a1.rw = a2.rw
LEFT JOIN eu ON a1.rw = eu.rw
