# Write your MySQL query statement below
select a.user_id,round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate from Signups as a left join Confirmations as c on a.user_id=c.user_id group by user_id;