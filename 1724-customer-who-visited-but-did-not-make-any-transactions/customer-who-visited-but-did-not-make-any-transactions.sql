# Write your MySQL query statement below
SELECT customer_id ,COUNT(*) as count_no_trans
FROM visits
LEFT JOIN Transactions USING(visit_id)
WHERE transaction_id IS NULL
GROUP BY Customer_id;