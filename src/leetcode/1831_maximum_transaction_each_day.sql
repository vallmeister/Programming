SELECT transaction_id
FROM
    (SELECT transaction_id, amount, MAX(amount) OVER (PARTITION BY day(day)) max_amt
    FROM Transactions) t1
WHERE amount = max_amt
ORDER BY 1
