# Climate change SQL project

SELECT * FROM state_climate;

SELECT state, year, tempc
AVG(tempc) OVER(
  PARTITION BY state
  ORDER BY year
) AS 'running_avg_temp'
FROM state_climate;

SELECT state, year, tempc,
FIRST_VALUE(tempc) OVER (
  PARTITION BY state
  ORDER BY tempc
) AS 'lowest_temp'
FROM state_climate;

SELECT state, year, tempc,
LAST_VALUE(tempc) OVER (
  PARTITION BY state
  ORDER BY tempc
  RANGE BETWEEN UNBOUNDED PRECEDING AND 
      UNBOUNDED FOLLOWING
) AS 'highest_temp'
FROM state_climate;

SELECT state, year, tempc, 
tempc - LAG(tempc, 1, tempc) OVER (
  PARTITION BY state
  ORDER BY year
) AS 'change_in_temp' FROM state_climate;

SELECT RANK() OVER (
  ORDER BY tempc ASC
) AS 'coldest_rank', tempc, year, state FROM state_climate;

SELECT RANK() OVER (
  ORDER BY tempc DESC
) AS 'warmest_rank', tempc, year, state FROM state_climate;

SELECT NTILE(4) OVER (
  PARTITION BY state
  ORDER BY tempc
) AS 'quartile', year, state, tempc 
FROM state_climate;

SELECT 
NTILE(5) OVER (
  ORDER BY tempc
  ) AS 'quintile',
state, year, tempc
FROM state_climate;