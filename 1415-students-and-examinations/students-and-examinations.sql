# Write your MySQL query statement below
Select s.student_id,s.student_name,x.subject_name,count(e.subject_name) as attended_exams 
from Students s join Subjects x  left join Examinations e
on x.subject_name=e.subject_name and s.student_id=e.student_id
group by s.student_id,x.subject_name
 order by s.student_id,x.subject_name;  