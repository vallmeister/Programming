SELECT followee AS follower, COUNT(*) num
FROM Follow
WHERE followee IN (SELECT followee FROM Follow)
AND followee IN (SELECT follower FROM Follow)
GROUP BY 1
ORDER BY 1
