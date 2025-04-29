# Write your MySQL query statement below
#their primary department. For employees who belong to one department, report their only department.
# when an employee belongs to only one department, their primary column is 'N'
#'Y', the department is the primary 
#'N', the department is not the primary.
select employee_id , department_id from Employee 
Where  primary_flag = "Y" 
or employee_id in (
select employee_id from Employee

group by employee_id
having count(*) = 1 )
