SELECT team_name, COUNT(*) matches_played,
       SUM(CASE WHEN outcome = 'win' THEN 3 WHEN outcome = 'draw' THEN 1 ELSE 0 END) points,
       SUM(home_team_goals) goal_for,
       SUM(away_team_goals) goal_against,
       SUM(home_team_goals) - SUM(away_team_goals) goal_diff
FROM (
    SELECT t.team_name,
           CASE WHEN home_team_goals > away_team_goals THEN 'win'
               WHEN home_team_goals = away_team_goals THEN 'draw'
                WHEN home_team_goals < away_team_goals THEN 'lose' END AS outcome,
        home_team_goals, away_team_goals
    FROM Matches m
    JOIN TEAMS t ON m.home_team_id = t.team_id
    UNION ALL
    SELECT t.team_name,
           CASE WHEN home_team_goals < away_team_goals THEN 'win'
               WHEN home_team_goals = away_team_goals THEN 'draw'
                WHEN home_team_goals > away_team_goals THEN 'lose' END AS outcome,
        away_team_goals AS home_team_goals, home_team_goals AS away_team_goals
    FROM Matches m
    JOIN TEAMS t ON m.away_team_id = t.team_id
     ) t1
GROUP BY 1
ORDER BY points DESC, goal_diff DESC, team_name
