SELECT member_id, name,
       CASE WHEN visits = 0 THEN 'Bronze' WHEN purchases / visits * 100 < 50 THEN 'Silver'
           WHEN purchases / visits * 100 < 80 THEN 'Gold' ELSE 'Diamond' END AS category
FROM
    (SELECT m.member_id, m.name, COUNT(v.visit_id) AS visits, COUNT(p.charged_amount) purchases
    FROM Members m
    LEFT JOIN Visits v ON m.member_id = v.member_id
    LEFT JOIN Purchases p ON v.visit_id = p.visit_id
    GROUP BY 1, 2
    ORDER BY 1) t1
