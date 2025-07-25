# Write your MySQL query statement below
with cte as
(
    select s.user_id, c.action from Signups s left join Confirmations c on s.user_id=c.user_id
)
select user_id, round(count(case when action="confirmed" then 1 end)/count(*),2) as confirmation_rate from cte group by user_id ;