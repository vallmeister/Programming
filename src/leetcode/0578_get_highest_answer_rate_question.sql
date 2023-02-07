SELECT question_id AS survey_log
FROM (
    SELECT question_id, COUNT(answer_id) / COUNT(*)
    FROM SurveyLog
    GROUP BY question_id
    ORDER BY 2 DESC, 1
    LIMIT 1
) t1
