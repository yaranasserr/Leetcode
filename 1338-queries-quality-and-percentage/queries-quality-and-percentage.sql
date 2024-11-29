# Write your MySQL query statement below
select query_name , 
round(avg(rating/position) ,2) as quality , 
ROUND(AVG(IF(rating < 3, 1, 0)) * 100, 2)as poor_query_percentage 
From Queries 
WHERE query_name IS NOT NULL
GROUP BY query_name;
