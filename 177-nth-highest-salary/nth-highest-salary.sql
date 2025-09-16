CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      WITH cte as
      (SELECT *,DENSE_RANK() OVER(ORDER BY salary DESC
      ) as rnk
      from Employee)

      SELECT DISTINCT IFNULL(salary,null)
      from cte
      where rnk=N

  );
END