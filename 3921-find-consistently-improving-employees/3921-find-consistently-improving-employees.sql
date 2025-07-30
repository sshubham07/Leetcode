# Write your MySQL query statement below
with cte as
(
    select p.employee_id,p.review_date,p.rating, e.name, rank() over(partition by e.employee_id order by p.review_date DESC) as rnk from performance_reviews p join employees e     on p.employee_id = e.employee_id
),
cte2 as
(
    select * from cte where rnk<=3
),
cte3 as
(
    select c1.employee_id, c1.name, c1.rating-c2.rating as improvement_score from cte2 c2 join cte2 c1 on c2.employee_id=c1.employee_id join cte2 c3 on c3.employee_id=c1.employee_id and c2.rnk=3 and c1.rnk=1 and c3.rnk = 2 and c1.rating>c3.rating and c3.rating>c2.rating where c1.rating-c2.rating >0  order by improvement_score DESC,c1.name
)
select * from cte3;
