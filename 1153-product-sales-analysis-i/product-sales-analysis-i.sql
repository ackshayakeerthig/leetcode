# Write your MySQL query statement below
SELECT product_name, year, price
FROM SALES
LEFT JOIN Product USING (Product_id)
GROUP BY sale_id,year;