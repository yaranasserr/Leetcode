# Write your MySQL query statement below


select p.product_id , 
 IFNULL(round(sum(p.price*u.units)/SUM(u.units),2),0) as average_price 
from Prices as p
left join UnitsSold as u 
on p.product_id = u.product_id 
AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

 
