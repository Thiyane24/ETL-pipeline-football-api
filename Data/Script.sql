SELECT name, team, goals 
        FROM TopScorers 
        ORDER BY goals DESC 
        LIMIT 1
        
SELECT name, team, assists 
        FROM TopScorers 
        ORDER BY assists DESC 
        LIMIT 1
        
  SELECT name, team, ROUND(minutes * 1.0 / goals, 2) AS mpg 
        FROM TopScorers 
        WHERE goals > 0
        ORDER BY mpg ASC 
        LIMIT 1
        
SELECT name, team, ROUND(minutes * 1.0 / assists, 2) AS mpa 
        FROM TopScorers 
        WHERE assists > 0
        ORDER BY mpa ASC 
        LIMIT 1