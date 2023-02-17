SELECT account_id, Transactions.day,
       SUM(CASE WHEN type = 'Deposit' THEN amount ELSE -amount END)
           OVER (PARTITION BY account_id ORDER BY Transactions.day) AS balance
FROM Transactions
ORDER BY 1
