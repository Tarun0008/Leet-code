# Write your MySQL query statement below
select a.customer_id,Count(a.customer_id) as count_no_trans from Visits a  left join Transactions b on a.visit_id=b.visit_id  where b.transaction_id is NULL group by a.customer_id;