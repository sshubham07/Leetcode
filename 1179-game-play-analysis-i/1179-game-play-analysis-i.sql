# Write your MySQL query statement below
with cte as (
    select player_id, event_date, rank() over (partition by player_id order by event_date) as first_login from Activity
    )
select player_id, event_date as first_login from cte where first_login=1;