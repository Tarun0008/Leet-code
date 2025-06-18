# Write your MySQL query statement below
select person_name from (select *, sum(weight) over (order by turn) ans from Queue) A
where A.ans<=1000
order by turn desc
limit 1;