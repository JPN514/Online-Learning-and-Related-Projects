-- Churn rate project
-- using temp tables to get churn rates for a company



 -- 1 Select first 100 rows to gain insight about the table:
--SELECT * FROM subscriptions LIMIT 10;

 -- 2 Determine which months we can calculate the chrun rate for using select min/max:
SELECT MIN(subscription_start), MAX(subscription_start)
FROM subscriptions;
-- calculating for jan, feb, mar 2017

-- 3 Create the temporary months table, this can be found in the lessons:
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
),

-- 4 cross join the subscriptions to the months table, careful with syntax:
cross_join AS (
  SELECT * FROM subscriptions
  CROSS JOIN months
),

--5, 6 create the temporary status table from cross_join for both segments with active/cancelled:
status AS (
SELECT id, 
first_day AS month,
CASE
  WHEN 
   (subscription_start < first_day) AND
   (subscription_end > first_day OR subscription_end IS NULL) AND (segment = 87) THEN 1
  ELSE 0 
  END AS is_active_87,
CASE
  WHEN 
 (subscription_start < first_day) AND
 (subscription_end > first_day OR subscription_end IS NULL) AND (segment = 30) THEN 1
  ELSE 0 
  END AS is_active_30,
CASE 
   WHEN 
   (subscription_end BETWEEN first_day AND last_day) AND (segment = 87) THEN 1
    ELSE 0
  END AS is_canceled_87,
CASE
    WHEN (subscription_end BETWEEN first_day AND last_day) AND (segment = 30) THEN 1
    ELSE 0
  END AS is_canceled_30
FROM cross_join
),

--7 status_aggregate table with counts for active and cancelled:  
status_aggregate AS (
SELECT month, SUM(is_active_87) as total_active_87, 
SUM(is_canceled_87) as total_canceled_87,
SUM(is_active_30) as total_active_30, 
SUM(is_canceled_30) as total_canceled_30
FROM status GROUP BY month
)

-- 8 calculate the churn rates:
SELECT month, 
  1.0 * total_canceled_87 / total_active_87 as churn_rate_87,
  1.0 * total_canceled_30 / total_active_30 as churn_rate_30
FROM status_aggregate GROUP BY month;

