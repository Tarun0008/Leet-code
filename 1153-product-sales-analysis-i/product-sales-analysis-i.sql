# Write your MySQL query statement below
Select a.product_name ,b.year,b.price from Sales b  join Product a on a.product_id=b.product_id;