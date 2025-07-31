# Write your MySQL query statement below
with cte as
(
    select e.employee_id,e.employee_name,e.department,sum(m.duration_hours) as week_total from employees e join meetings m on e.employee_id=m.employee_id group by e.employee_id,e.employee_name,e.department,WEEK(meeting_date, 3)
),
cte2 as
(
    select employee_id,employee_name,department, count(CASE WHEN week_total>20 THEN 1 END) as meeting_heavy_weeks from cte group by employee_id,employee_name,department
)
select * from cte2 where meeting_heavy_weeks>=2 order by meeting_heavy_weeks DESC,employee_name ASC;