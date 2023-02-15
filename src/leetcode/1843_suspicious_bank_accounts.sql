SELECT DISTINCT account_id
FROM
    (SELECT t1.*, RANK() OVER (PARTITION BY a.account_id ORDER BY t1.mon) rk
    FROM
        (SELECT DATE_FORMAT(day, "%Y-%m") mon, transaction_id, account_id,
            SUM(CASE WHEN type = 'Creditor' THEN amount ELSE 0 END) total
        FROM Transactions
        GROUP BY DATE_FORMAT(day, "%Y-%m"), account_id ) t1
    JOIN Accounts a ON a.account_id = t1.account_id
    WHERE max_income < total) t2
GROUP BY account_id, mon - INTERVAL rk month
HAVING COUNT(*) >= 2
ORDER BY transaction_id
