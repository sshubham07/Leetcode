# Write your MySQL query statement below
with cte as
(
    select "Fall" as season, p.category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue from sales s join products p on s.product_id = p.product_id where Month(s.sale_date) in (9,10,11) group by p.category order by total_quantity DESC, total_revenue DESC limit 1 
),
cte2 as
(
    select "Winter" as season, p.category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue from sales s join products p on s.product_id = p.product_id where Month(s.sale_date) in (12,1,2) group by p.category order by total_quantity DESC, total_revenue DESC limit 1 
),
cte3 as
(
    select "Summer" as season, p.category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue from sales s join products p on s.product_id = p.product_id where Month(s.sale_date) in (6,7,8) group by p.category order by total_quantity DESC, total_revenue DESC limit 1 
),
cte4 as
(
    select "Spring" as season, p.category, sum(s.quantity) as total_quantity, sum(quantity*price) as total_revenue from sales s join products p on s.product_id = p.product_id where Month(s.sale_date) in (3,4,5) group by p.category order by total_quantity DESC, total_revenue DESC limit 1 
)
select * from cte
UNION ALL
select * from cte4
UNION ALL
select * from cte3
UNION ALL
select * from cte2;

