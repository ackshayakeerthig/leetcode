# Write your MySQL query statement below
with cte as
(select * , DENSE_RANK() OVER (ORDER BY Salary DESC)
as r
from Employee)

SELECT  IFNULL((SELECT Salary  
 from cte
where r=2
LIMIT 1),null) 
as SecondHighestSalary
;
