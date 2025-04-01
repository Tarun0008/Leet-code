# Write your MySQL query statement below
Select a.name from Employee a join Employee b on a.id=b.managerid group by  a.id,a.name having count(b.managerid)>=5;