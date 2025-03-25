# Write your MySQL query statement below
Select a.student_id,a.student_name,s.subject_name,count(b.subject_name) as attended_exams  from Students a cross join subjects s left join Examinations b on a.student_id=b.student_id and s.subject_name=b.subject_name group by b.subject_name,a.student_id,s.subject_name order by a.student_id, s.subject_name;
