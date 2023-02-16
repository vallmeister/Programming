SELECT *
FROM Friendship f1, Friendship f2
WHERE f1.user1_id != f2.user1_id AND f1.user2_id != f2.user2_id
ORDER BY 1, 2


    ((f1.user1_id, f2.user2_id) IN (SELECT * FROM Friendship) OR (f2.user2_id, f1.user1_id) IN (SELECT * FROM Friendship))
AND ((f2.user1_id, f1.user2_id) IN (SELECT * FROM Friendship) OR (f1.user2_id, f2.user1_id) IN (SELECT * FROM Friendship))
