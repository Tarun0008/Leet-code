# Write your MySQL query statement below
delete p from Person P join Person p2 on p.email=p2.email where  p.id>p2.id;