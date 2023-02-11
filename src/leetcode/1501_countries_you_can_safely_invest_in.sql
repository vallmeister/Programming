SELECT *
FROM Calls c1
JOIN Person p1 ON p1.id = c1.caller_id
JOIN Person p2 ON p2.id = c1.callee_id
JOIN Country c2 ON LEFT(p1.phone_number, 3) = c2.country_code
JOIN Country c3 ON LEFT(p2.phone_number, 3) = c3.country_code
