SELECT COUNT(*) accounts_count
FROM
    (SELECT account_id
    FROM Subscriptions
    WHERE year(end_date) >= 2021
    AND year(start_date) <= 2021
    AND account_id NOT IN (
        SELECT account_id
        FROM Streams
        WHERE year(stream_date) = 2021
        )
    ) t1
