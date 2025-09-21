# Write your MySQL query statement below
select w1.id
from weather w1
LEFT JOIN weather w2
on w1.recorddate-INTERVAL 1 DAY=w2.recorddate
where w1.temperature > w2.temperature;