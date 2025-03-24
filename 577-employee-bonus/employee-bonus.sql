# Write your MySQL query statement below
select a.name,b.bonus from Employee a left join Bonus b on a.empid=b.empid where b.bonus<1000 or b.bonus is null;