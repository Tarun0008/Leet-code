select d.name as Department,
e.name as Employee,
e.salary as Salary
from employee e 
join department d on e.departmentId=d.id

where (select  count(distinct(salary))
from employee e2
where e2.salary>=e.salary and e.departmentId=e2.departmentId
)<=3 
order by  Department,Salary desc
