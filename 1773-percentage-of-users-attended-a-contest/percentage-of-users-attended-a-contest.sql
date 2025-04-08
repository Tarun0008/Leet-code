select b.contest_id, round(count(distinct b.user_id)*100/(select count(*) from users),2) as percentage from 
Register b
group by b.contest_id
order by percentage desc,
b.contest_id asc;