-- # Write your MySQL query statement below
-- select t.request_at as Day
-- ,(count(cancelled)/(select join Users as u 
-- on 
-- u.users_id = t.client_id and u.users_id = t.driver_id  count(t.id) where u.banned='No') as concat ('Cancellation ' ,'Rate') 

-- from Trips as t 
-- join Users as u 
-- on 
-- u.users_id = t.client_id and u.users_id = t.driver_id 
-- where (t.status = 'cancelled_by_driver' and t.status ='cancelled_by_client' ) as cancelled 
-- and u.banned='No'
-- and request_at between "2013-10-01"  and "2013-10-03" ;

SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(CASE WHEN t.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END) /
        COUNT(t.id), 2) AS "Cancellation Rate"
FROM 
    Trips AS t
JOIN 
    Users AS uc ON t.client_id = uc.users_id AND uc.banned = 'No'
JOIN 
    Users AS ud ON t.driver_id = ud.users_id AND ud.banned = 'No'
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.request_at;
