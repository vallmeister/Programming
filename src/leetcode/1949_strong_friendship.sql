SELECT user1_id, user2_id, COUNT(*) common_friend
FROM
    (SELECT f1.user1_id, f1.user2_id
     FROM Friendship f1
              JOIN Friendship f2 ON f1.user2_id = f2.user1_id
     WHERE (f1.user1_id, f2.user2_id) IN (SELECT * FROM Friendship)
     OR (f2.user2_id, f1.user1_id) IN (SELECT * FROM Friendship)
     UNION ALL
     SELECT f1.user1_id, f1.user2_id
     FROM Friendship f1
              JOIN Friendship f2 ON f1.user2_id = f2.user2_id
     WHERE (f1.user1_id, f2.user1_id) IN (SELECT * FROM Friendship)
     OR (f2.user1_id, f1.user1_id) IN (SELECT * FROM Friendship)
     ) t1
GROUP BY 1, 2
HAVING common_friend >= 3
ORDER BY 1, 2
