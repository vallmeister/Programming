WITH platform AS (
    SELECT 'Android' AS platform
    UNION
    SELECT 'IOS' AS platform
    UNION
    SELECT 'Web' AS platform
),
experiment AS (
    SELECT 'Reading' AS experiment_name
    UNION
    SELECT 'Sports' AS experiment_name
    UNION
    SELECT 'Programming' AS experiment_name
),
t1 AS (
    SELECT *
    FROM platform p, experiment e
    ORDER BY p.platform, e.experiment_name
)
SELECT t1.platform, t1.experiment_name, COUNT(e.experiment_id) num_experiments
FROM t1
LEFT JOIN Experiments e
ON e.platform = t1.platform
AND e.experiment_name = t1.experiment_name
GROUP BY 1, 2
