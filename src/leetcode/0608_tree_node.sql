WITH children AS (
    SELECT t1.id, t1.p_id, t2.id child
    FROM Tree t1
    LEFT JOIN Tree t2 ON t1.id = t2.p_id)

SELECT id, CASE WHEN COUNT(p_id) = 0 THEN 'Root' WHEN COUNT(child) = 0 THEN 'Leaf' ELSE 'Inner' END AS type
FROM children
GROUP BY 1
ORDER BY 1
