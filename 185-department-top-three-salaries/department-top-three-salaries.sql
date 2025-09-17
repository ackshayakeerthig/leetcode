# Write your MySQL query statement below
select d.name as Department , e1.name as Employee, Salary
from employee e1
left join department d
on e1.departmentid=d.id
where (
    select count(distinct e2.salary)
    from employee e2
    where e1.departmentid=e2.departmentid
    and e1.salary<e2.salary
) < 3
