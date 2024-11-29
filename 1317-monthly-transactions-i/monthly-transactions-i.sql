# Write your MySQL query statement below
select 
left(trans_date,7) as month , 
country ,
count(state) as trans_count ,
COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count,
sum(amount) as trans_total_amount ,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount

from Transactions
group by  left(trans_date,7) , country ;
