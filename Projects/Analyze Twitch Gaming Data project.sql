-- Analyze Twitch Gaming Data project 

-- Using SQL to analyse game genres and viewing time counts on twitch 



-- 1 familiarise yourself with the tables:
SELECT * FROM stream LIMIT 20;
SELECT * FROM chat LIMIT 20;

-- 2 unique games in the stream table:
SELECT DISTINCT game FROM stream;

-- 3 unique channels in the stream table:
SELECT DISTINCT channel FROM stream;

-- 4 most popular games in the stream table:
SELECT game, COUNT(game) as streamers 
FROM stream
GROUP BY game
ORDER BY 2 DESC;

-- 5 locations of viewers of LoL streamers:
SELECT country, COUNT(*) as 'no. of viewers' FROM stream
WHERE game = 'League of Legends'
GROUP BY country
ORDER BY 2 DESC;

-- 6 list of players and their number of streamers:
SELECT player, COUNT(*) AS 'no. of streamers'
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- 7 group the games by genre e.g. fps, rpg, moba:
SELECT game, 
 CASE 
  WHEN game = 'League of Legends' 
  THEN 'MOBA'
  WHEN game = 'Dota 2' 
  THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
  THEN 'MOBA'
  WHEN game = 'Counter Strike: Global Offensive'
  THEN 'FPS'
  WHEN game = 'DayZ'
  THEN 'Survival'
  WHEN game = 'ARK: Survival Evolved'
  THEN 'Survival'
  ELSE 'Other'
 END AS 'genre',
 COUNT(*)
FROM stream
GROUP BY game
ORDER BY 3 DESC;

-- 8 take a look at the time column from the stream table:
SELECT time
FROM stream
LIMIT 10;   -- format is: YYYY-MM-DD HH:MM:SS

-- 9 format the time column using strftime() function from SQLite:
SELECT time,
   strftime('%S', time)  
FROM stream
GROUP BY 1
LIMIT 20; -- returns the seconds of the time column 

-- 10 query to return the view count for each hour using strftime() function with country as GB:
SELECT strftime('%H', time) as hour,
   COUNT(*) as 'View_count_by_hour'
FROM stream
WHERE country = 'GB'
GROUP BY 1;

-- 11 join the stream and chat tables on the device_id column:
SELECT * FROM stream st
JOIN chat ch ON 
st.device_id = ch.device_id;

