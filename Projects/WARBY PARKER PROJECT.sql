-- WARBY PARKER PROJECT

-- Using funnels to analyse data 

-- 1 check out quiz funnel
SELECT * FROM survey LIMIT 10;

-- 2 count how many users move to next question
SELECT question, COUNT(DISTINCT user_id) AS 'users_progressed_to_step' FROM survey GROUP BY question;

-- 3
-- calculate percentages 

-- 4 check out the 3 tables
SELECT * FROM quiz LIMIT 5;
SELECT * FROM home_try_on LIMIT 5;
SELECT * FROM purchase LIMIT 5;

-- 5 left join the 3 tables
WITH funnels AS ( 
  SELECT DISTINCT q.user_id, 
    h.user_id IS NOT NULL AS 'is_home_try_on',
    h.number_of_pairs,
    p.user_id IS NOT NULL AS 'is_purchase'
  FROM quiz AS 'q'
  LEFT JOIN home_try_on AS 'h' 
   ON h.user_id = q.user_id
  LEFT JOIN purchase AS 'p' 
   ON p.user_id = h.user_id)
SELECT * FROM funnels LIMIT 10;   

-- 6 compare conversion rates for each step:
WITH funnels AS ( 
  SELECT DISTINCT q.user_id, 
    h.user_id IS NOT NULL AS 'is_home_try_on',
    h.number_of_pairs,
    p.user_id IS NOT NULL AS 'is_purchase'
  FROM quiz AS 'q'
  LEFT JOIN home_try_on AS 'h' 
   ON h.user_id = q.user_id
  LEFT JOIN purchase AS 'p' 
   ON p.user_id = h.user_id)
SELECT COUNT(*) AS 'num_browse',
   SUM(is_home_try_on) AS 'num_try_on',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_home_try_on) / COUNT(user_id) AS 'browse_to_home_try_on',
   1.0 * SUM(is_purchase) / SUM(is_home_try_on) AS 'home_try_on_to_purchase'
   FROM funnels;  

-- 6 compare purchase rates for 3 pairs vs 5 pairs:
WITH funnels AS ( 
  SELECT DISTINCT q.user_id, 
    h.user_id IS NOT NULL AS 'is_home_try_on',
    h.number_of_pairs AS 'num_pairs',
    p.user_id IS NOT NULL AS 'is_purchase'
  FROM quiz AS 'q'
  LEFT JOIN home_try_on AS 'h' 
   ON h.user_id = q.user_id
  LEFT JOIN purchase AS 'p' 
   ON p.user_id = h.user_id)
SELECT num_pairs, COUNT(DISTINCT user_id) AS 'num_purchase' FROM funnels WHERE is_purchase IS NOT 0 GROUP BY num_pairs;


