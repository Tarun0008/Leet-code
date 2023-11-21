# Write your MySQL query statement below
Select x,y,z, case when ((x+y>z) and (x+z>y) and (z+y>x)) then 'Yes' else 'No' END as triangle from Triangle;