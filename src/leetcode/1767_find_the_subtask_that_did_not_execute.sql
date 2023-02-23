WITH RECURSIVE t1 AS (
    SELECT task_id, subtasks_count AS subtask_id
    FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id - 1 FROM t1 WHERE subtask_id > 1
)
SELECT task_id, subtask_id
FROM t1
WHERE (task_id, subtask_id) NOT IN (SELECT * FROM Executed)
