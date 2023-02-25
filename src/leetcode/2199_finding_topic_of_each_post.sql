WITH t1 AS (
    SELECT DISTINCT p.post_id, LOWER(p.content), k.topic_id
    FROM Posts p
    LEFT JOIN Keywords k
    ON CONCAT(' ', LOWER(p.content), ' ') LIKE CONCAT('% ', LOWER(k.word), ' %')
)
SELECT post_id, CASE WHEN topic_id IS NULL THEN 'Ambiguous!' ELSE
    GROUP_CONCAT(topic_id ORDER BY topic_id SEPARATOR ',') END topic
FROM t1
GROUP BY 1
