SELECT DISTINCT viewer_id id
FROM (
    SELECT DISTINCT *
    FROM Views
     ) t1
GROUP BY viewer_id, view_date
HAVING  COUNT(*) > 1
ORDER BY 1
