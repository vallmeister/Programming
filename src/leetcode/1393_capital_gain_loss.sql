WITH buys AS (
    SELECT stock_name, SUM(price) loss
    FROM Stocks
    WHERE operation = 'Buy'
    GROUP BY 1
),
sells AS (
    SELECT stock_name, SUM(price) gain
    FROM Stocks
    WHERE operation = 'Sell'
    GROUP BY 1
)

SELECT b.stock_name, s.gain - b.loss AS capital_gain_loss
FROM buys b
JOIN sells s ON b.stock_name = s.stock_name
