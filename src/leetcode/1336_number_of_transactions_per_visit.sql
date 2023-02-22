WITH RECURSIVE t2 AS (SELECT 0 AS transactions_count
                      UNION ALL
                      SELECT transactions_count + 1
                      FROM t2
                      WHERE transactions_count < (
                          SELECT MAX(cnt) FROM (SELECT COUNT(*) cnt
                                                FROM Transactions
                                                GROUP BY user_id, transaction_date)
                              cte)
                      ),
    t1 AS (
        SELECT 0 AS transactions_count, COUNT(*) visits_count
        FROM Visits
        WHERE (user_id, visit_date) NOT IN (SELECT user_id, transaction_date FROM Transactions)
        UNION ALL
        SELECT DISTINCT COUNT(*) transactions_count,
               COUNT(*) OVER (PARTITION BY COUNT(*)) visits_count
        FROM Transactions
        GROUP BY user_id, transaction_date
    )
SELECT t2.transactions_count, COALESCE(t1.visits_count, 0) visits_count
FROM t2
LEFT JOIN t1
ON t1.transactions_count = t2.transactions_count
