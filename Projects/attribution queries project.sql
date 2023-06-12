-- ATTRIBUTION QUERIES PROJECT 
-- where from, when, how users visited a website


-- step 1 count number of different campaigns and sources:
SELECT COUNT(DISTINCT(utm_campaign)) AS 'no. of campaigns' FROM page_visits;
SELECT COUNT(DISTINCT(utm_source)) AS 'no. of sources' FROM page_visits;
SELECT DISTINCT utm_campaign,utm_source FROM page_visits;

-- step 2 distinct values of page_name column:
SELECT DISTINCT page_name FROM page_visits;


-- step 3 How many first touches is each campaign responsible for?

WITH first_touch AS (
    SELECT user_id,
        MIN(timestamp) as first_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT COUNT(ft.first_touch_at) AS first_touch_count,
    pv.utm_source,
		pv.utm_campaign
FROM first_touch ft
JOIN page_visits pv
    ON ft.user_id = pv.user_id
    AND ft.first_touch_at = pv.timestamp
    GROUP BY pv.utm_campaign
    ORDER BY 1 DESC;

-- step 4 How many last touches is each campaign responsible for?  

WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT COUNT(lt.last_touch_at) AS last_touch_count,
    pv.utm_source,
		pv.utm_campaign
FROM last_touch lt
JOIN page_visits pv
    ON lt.user_id = pv.user_id
    AND lt.last_touch_at = pv.timestamp
    GROUP BY pv.utm_campaign
    ORDER BY 1 DESC;

-- step 5 How many visitors make a purchase?   
SELECT COUNT(DISTINCT user_id) FROM page_visits 
WHERE page_name = '4 - purchase'; -- 361 made a purchase

-- step 6 How many last touches on the purchase page is each campaign responsible for?

WITH last_touch AS (
    SELECT user_id,
        MAX(timestamp) as last_touch_at
    FROM page_visits
    GROUP BY user_id)
SELECT COUNT(lt.last_touch_at) AS last_touch_count_purchase,
    pv.utm_source,
		pv.utm_campaign
FROM last_touch lt  
JOIN page_visits pv
    ON lt.user_id = pv.user_id
    AND lt.last_touch_at = pv.timestamp
    WHERE page_name = '4 - purchase'
    GROUP BY pv.utm_campaign
    ORDER BY 1 DESC;

-- step 7:
-- reinvest in email newsletter, fb retargetting-ad, email retargetting-campaign, nytimes getting-to-know article, google paid search.