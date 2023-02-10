WITH t1 AS (
    SELECT c1.customer_id, COUNT(c2.contact_name) AS trusted_contacts_cnt
    FROM Customers c1
    LEFT JOIN Contacts c2 ON c1.customer_id = c2.user_id AND c2.contact_email IN (SELECT email FROM Customers)
    GROUP BY 1
)
SELECT i.invoice_id, c1.customer_name, i.price, COUNT(c2.user_id) AS contacts_cnt, t1.trusted_contacts_cnt
FROM Invoices i
LEFT JOIN Customers c1 ON i.user_id = c1.customer_id
LEFT JOIN Contacts c2 ON c1.customer_id = c2.user_id
LEFT JOIN t1 ON c1.customer_id = t1.customer_id
GROUP BY 1, 2, 3
ORDER BY 1
