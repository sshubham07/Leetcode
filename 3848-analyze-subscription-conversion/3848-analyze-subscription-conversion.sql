# Write your MySQL query statement below
with cte as
(
    select user_id, round(avg(activity_duration),2) AS trial_avg_duration FROM UserActivity where activity_type="free_trial" GROUP BY user_id
),
cte2 AS
(
    select user_id, round(avg(activity_duration),2) AS paid_avg_duration FROM UserActivity where activity_type="paid" GROUP BY user_id
)
SELECT cte.user_id, cte.trial_avg_duration, cte2.paid_avg_duration from cte JOIN cte2 ON cte.user_id = cte2.user_id;