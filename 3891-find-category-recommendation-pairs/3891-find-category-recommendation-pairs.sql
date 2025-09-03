# Write your MySQL query statement below
with cte as 
(
    select p.user_id, i.category from ProductPurchases p join ProductInfo i on p.product_id=i.product_id
),
cte2 as
(
    select distinct c1.user_id, c1.category as category1, c2.category as category2 from cte c1 join cte c2 on c1.user_id = c2.user_id and c1.category<c2.category
)
select category1,category2, count(*) as customer_count from cte2 group by category1,category2 having customer_count>=3 order by customer_count DESC,category1,category2;