-- ADVANCED SQL LESSONS 


-- WINDOW FUNCTIONS  


SELECT username, SUM(change_in_followers) FROM social_media WHERE username = "instagram" GROUP BY username;

SELECT 
   month,
   change_in_followers,
   SUM(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_total'
FROM
   social_media
WHERE
   username = 'instagram';

SELECT month,
  change_in_followers,
  AVG(change_in_followers) OVER (
    ORDER BY month
  ) AS running_avg
FROM social_media
WHERE username = 'instagram';

SELECT 
   month,
   change_in_followers,
   SUM(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_total',
   AVG(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_avg',
   COUNT(change_in_followers) OVER (
      ORDER BY month
   ) AS 'running_count'
FROM
   social_media
WHERE
   username = 'instagram';

--PARTITION BY is analogous to group by but does not restrict the results:

SELECT 
    username,
    month,
    change_in_followers,
    SUM(change_in_followers) OVER (
      PARTITION BY username 
      ORDER BY month
    ) 'running_total_followers_change',
    AVG(change_in_followers) OVER (
      PARTITION BY username
      ORDER BY month
    ) 'running_avg_followers_change'
FROM
    social_media;


SELECT username,
   posts,
   FIRST_VALUE (posts) OVER (
      PARTITION BY username 
      ORDER BY posts
   ) AS 'fewest_posts'
FROM social_media;

SELECT
   username,
   posts,
   LAST_VALUE (posts) OVER (
      PARTITION BY username 
      ORDER BY posts
      RANGE BETWEEN UNBOUNDED PRECEDING AND 
      UNBOUNDED FOLLOWING
    ) most_posts
FROM
    social_media;

-- LEAD(after) AND LAG(before) :

SELECT
   artist,
   week,
   streams_millions,
   LAG(streams_millions, 1, 0) OVER (
      ORDER BY week 
   ) previous_week_streams 
FROM
   streams 
WHERE
   artist = 'Lady Gaga';

SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER ( 
      ORDER BY week 
   ) streams_millions_change
FROM
   streams 
WHERE
   artist = 'Lady Gaga';

SELECT
   artist,
   week,
   streams_millions,
   streams_millions - LAG(streams_millions, 1, streams_millions) OVER ( 
      PARTITION BY artist
      ORDER BY week 
   ) AS 'streams_millions_change',
   chart_position,
   LAG(chart_position, 1, chart_position) OVER ( 
      PARTITION BY artist
      ORDER BY week 
) - chart_position AS 'chart_position_change'
FROM
   streams
WHERE 
   artist = 'Lady Gaga';

SELECT
   artist,
   week,
   streams_millions,
   LEAD(streams_millions, 1) OVER (
      PARTITION BY artist
      ORDER BY week
   ) - streams_millions AS 'streams_millions_change',
   chart_position,
   chart_position - LEAD(chart_position, 1) OVER ( 
      PARTITION BY artist
      ORDER BY week 
) AS 'chart_position_change'
FROM
   streams;

-- ROW NUMBER() sequentially orders your results:

SELECT 
   ROW_NUMBER() OVER (
      ORDER BY streams_millions DESC
   ) AS 'row_num', 
   artist, 
   week,
   streams_millions
FROM
   streams;

-- RANK() similar to ROW NUMBER() only equal results have the same row numbering:

SELECT 
   RANK() OVER (
      PARTITION BY week
      ORDER BY streams_millions DESC
   ) AS 'rank', 
   artist, 
   week,
   streams_millions
FROM
   streams;

-- NTILE() acts as a percentile finder here returning quartiles.
-- partition by creates quartiles for each week 1 through 8
SELECT 
   NTILE(4) OVER (
      PARTITION BY week
      ORDER BY streams_millions DESC
   ) AS 'quartile', 
   artist, 
   week,
   streams_millions
FROM
   streams;

-- Mathematical functions:

SELECT (price * quantity) FROM bakery;


SELECT first_name, ABS(guess - 804) FROM guesses;
SELECT ABS(AVG(guess)-804) FROM guesses;

SELECT item_name, (price - CAST(discount AS REAL)) * quantity FROM bakery; -- cast converts the data into the desired datatype

SELECT DATE(order_date) FROM bakery; -- gets the date part of a datetime

SELECT DATETIME(order_date, 'start of day', '+2 days', '+7 hours') FROM bakery;   -- can use modifiers to alter the date and time ie for collection of orders from the bakery 

SELECT strftime('%d', order_date) AS 'order_day',
  COUNT(*) 
FROM bakery 
GROUP BY 1
ORDER BY 2 DESC;



-- USAGE FUNNELS LESSON:

SELECT question_text, COUNT(DISTINCT user_id) FROM survey_responses GROUP BY question_text;

SELECT modal_text, COUNT(DISTINCT user_id) FROM onboarding_modals GROUP BY modal_text ORDER BY modal_text;

SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks'
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;

SELECT modal_text,
  COUNT(DISTINCT CASE
    WHEN ab_group = 'control' THEN user_id
    END) AS 'control_clicks',
  COUNT(DISTINCT CASE
    WHEN ab_group = 'variant' THEN user_id
    END) AS 'variant_clicks'  
FROM onboarding_modals
GROUP BY 1
ORDER BY 1;            -- the cases funnel the clicks at each stage of the process to count how many users progress to each stage

-- multiple table funnels below:

SELECT DISTINCT b.browse_date,
   b.user_id,
   c.user_id IS NOT NULL AS 'is_checkout',
   p.user_id IS NOT NULL AS 'is_purchase'
FROM browse AS 'b'
LEFT JOIN checkout AS 'c'
  ON c.user_id = b.user_id
LEFT JOIN purchase AS 'p'
  ON p.user_id = c.user_id
LIMIT 50;


-- Below uses the funnel to group the table ahead of time using left joins, then we select from the funnel to calculate % of users going from stage to stage 

WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT COUNT(*) AS 'num_browse', SUM(is_checkout) AS 'num_checkout', 
       SUM(is_purchase) AS 'num_purchase', 1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase' FROM funnels;


-- similar to the above except we get each stage grouped by the browse date (%s for each date in the table)
WITH funnels AS (
  SELECT DISTINCT b.browse_date,
     b.user_id,
     c.user_id IS NOT NULL AS 'is_checkout',
     p.user_id IS NOT NULL AS 'is_purchase'
  FROM browse AS 'b'
  LEFT JOIN checkout AS 'c'
    ON c.user_id = b.user_id
  LEFT JOIN purchase AS 'p'
    ON p.user_id = c.user_id)
SELECT browse_date, COUNT(*) AS 'num_browse',
   SUM(is_checkout) AS 'num_checkout',
   SUM(is_purchase) AS 'num_purchase',
   1.0 * SUM(is_checkout) / COUNT(user_id) AS 'browse_to_checkout',
   1.0 * SUM(is_purchase) / SUM(is_checkout) AS 'checkout_to_purchase'
FROM funnels GROUP BY browse_date;


-- USER CHURN LESSON below

SELECT (100. / 2000);   -- number of cancellations divided by the number of subscriotions 
SELECT 450. / 3000; 

-- This gets the cancelled subsrciptions for the month of Jan 2017 first and divides it by the total number of subscriptions 
-- 
SELECT 1.0 * (
  SELECT COUNT(*) 
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    subscription_end 
    BETWEEN '2017-01-01' 
    AND '2017-01-31'
  )
) / (
  SELECT COUNT(*)
  FROM subscriptions 
  WHERE subscription_start < '2017-01-01'
  AND (
    (subscription_end >= '2017-01-01')
    OR (subscription_end IS NULL)
  )
) 
AS result;

-- Similar to above but utilises temporary tables to aid reusability:
-- Mold the previous statements into a more resuable structure 
-- temporary table of active subscriptions:
WITH enrollments AS
(SELECT *
FROM subscriptions
WHERE subscription_start < '2017-01-01'
AND (
  (subscription_end >= '2017-01-01')
  OR (subscription_end IS NULL)
)),
-- status of subscriptions using enrollments temp table from above:
status AS 
(SELECT
CASE
  WHEN (subscription_end > '2017-01-31')
    OR (subscription_end IS NULL) THEN 0
    ELSE 1
  END as is_canceled,
CASE
    WHEN subscription_start < '2017-01-01'
      AND (
        (subscription_end >= '2017-01-01')
        OR (subscription_end IS NULL)
      ) THEN 1
    ELSE 0
  END as is_active
  FROM enrollments
  )
  -- calculation below:
SELECT 1.0 * SUM(is_canceled) / SUM(is_active)
FROM status;


-- create temp table of relevant months to aid the calculations:
-- Need this as some SQL engines do not contain prebulit months tables.
WITH months AS (
SELECT
  '2017-01-01' AS first_day,
  '2017-01-31' AS last_day
UNION
SELECT
  '2017-02-01' AS first_day,
  '2017-02-28' AS last_day
UNION  
SELECT
  '2017-03-01' AS first_day,
  '2017-03-31' AS last_day
) 
SELECT * FROM months;


-- cross join table below has combination of all subscriptions and months possible, can determine the status of any subscription in each month:
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS (
  SELECT * FROM subscriptions 
  CROSS JOIN months
)
SELECT *
FROM cross_join
LIMIT 100;


-- add an is_active column using the month from the cross_join table aliased as first_day. 
-- All amounts to a status table!
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS (
  SELECT id, first_day as month
CASE
    WHEN (subscription_start < first_day)
      AND (
        (subscription_end > first_day)
        OR (subscription_end IS NULL)
      ) THEN 1
    ELSE 0
  END as is_active
  FROM cross_join
)
SELECT *
FROM status
LIMIT 100;


-- added an is_cancelled column to the status table:
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day,last_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
 WHEN (subscription_end BETWEEN first_day AND last_day) 
 THEN 1
 ELSE 0 
END AS is_canceled
FROM cross_join)
SELECT *
FROM status
LIMIT 100;

-- added the status_aggregate table at the bottom. This is the sums by month of active and cancellations. 
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS 
(SELECT month, SUM(is_active) as active, 
SUM(is_canceled) as canceled
FROM status GROUP BY month)
SELECT *
FROM status_aggregate;

-- select the churn rate calculation:
WITH months AS
(SELECT
  '2017-01-01' as first_day,
  '2017-01-31' as last_day
UNION
SELECT
  '2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
SELECT
  '2017-03-01' as first_day,
  '2017-03-31' as last_day
),
cross_join AS
(SELECT *
FROM subscriptions
CROSS JOIN months),
status AS
(SELECT id, first_day as month,
CASE
  WHEN (subscription_start < first_day)
    AND (
      subscription_end > first_day
      OR subscription_end IS NULL
    ) THEN 1
  ELSE 0
END as is_active,
CASE 
  WHEN subscription_end BETWEEN first_day AND last_day THEN 1
  ELSE 0
END as is_canceled
FROM cross_join),
status_aggregate AS
(SELECT
  month,
  SUM(is_active) as active,
  SUM(is_canceled) as canceled
FROM status
GROUP BY month)
SELECT month, 1.0 * canceled / active as churn_rate   -- calculates the churn rate here
FROM status_aggregate GROUP BY month;


-- MARKETING ATTRIBUTION LESSON ::
-- this allows web developers, designers and analysts to determine WHERE, WHEN and HOW users visited the site from e.g ads, emails, other websites
-- first touch: how usersa are drawn in, last touch: how users are tempted back to a website

SELECT *
FROM page_visits
WHERE user_id = 10069 
   AND utm_source = 'buzzfeed'; -- checks for a specific user in the table and retreives their id and source, in this case buzzfeed which is the first touch


SELECT *
FROM page_visits
WHERE user_id = 10069; -- this retreives all info including the last touch (last source before a purchase in this case)


SELECT *
FROM page_visits
WHERE user_id = 10329;


SELECT user_id,
   MIN(timestamp) AS 'first_touch_at'  -- gets time for each users first touch to our website 
FROM page_visits
GROUP BY user_id;


SELECT user_id, 
  MAX(timestamp) AS 'last_touch_at'    -- gets time for a specific users last touch to our website
FROM page_visits WHERE user_id = 10069
GROUP BY user_id;


-- attribution query for first_touch attribution 
WITH first_touch AS (                     -- this query gets the user_id, timestamp and source using a temp table and cross joins
    SELECT user_id,
       MIN(timestamp) AS 'first_touch_at'
    FROM page_visits
    GROUP BY user_id)
SELECT ft.user_id,
   ft.first_touch_at,
   pv.utm_source
FROM first_touch AS 'ft'
JOIN page_visits AS 'pv'
   ON ft.user_id = pv.user_id
   AND ft.first_touch_at = pv.timestamp;


-- attribution query for last_touch attribution 
WITH last_touch AS (
    SELECT user_id,
       MAX(timestamp) AS 'last_touch_at'
    FROM page_visits
    GROUP BY user_id)
SELECT lt.user_id,
   lt.last_touch_at,
   pv.utm_source
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
   ON lt.user_id = pv.user_id
   AND lt.last_touch_at = pv.timestamp;


-- same last_touch attribution query but with a where clause for a specific user
WITH last_touch AS (
    SELECT user_id,
       MAX(timestamp) AS 'last_touch_at'
    FROM page_visits
    GROUP BY user_id)
SELECT lt.user_id,
   lt.last_touch_at,
   pv.utm_source
FROM last_touch AS 'lt'
JOIN page_visits AS 'pv'
   ON lt.user_id = pv.user_id
   AND lt.last_touch_at = pv.timestamp
   WHERE lt.user_id = 10069;


