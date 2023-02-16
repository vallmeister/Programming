SELECT order_id
FROM (SELECT order_id, MAX(quantity) max_quant, MAX(AVG(quantity)) OVER () max_avg
      FROM OrdersDetails
      GROUP BY 1) t1
WHERE max_quant > max_avg
