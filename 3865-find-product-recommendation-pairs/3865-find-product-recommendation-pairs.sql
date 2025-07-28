# Write your MySQL query statement below
with cte as 
(
    select p1.user_id as u1, p1.product_id as product1, p1.quantity as q1,p2.user_id as u2, p2.product_id as product2, p2.quantity as q2 from ProductPurchases p1 join ProductPurchases p2 on p1.product_id<p2.product_id and p1.user_id=p2.user_id
),
cte2 as
(
    select u1,product1, q1,u2,product2, q2, info1.category as c1, info2.category as c2 from cte join ProductInfo info1 on product1=info1.product_id join ProductInfo info2 on product2=info2.product_id
)
select  product1 as product1_id, product2 as product2_id,c1 as product1_category, c2 as product2_category,count(*) as customer_count from cte2 group by product1_id,product2_id,product1_category,product2_category having count(*)>=3 order by customer_count DESC, product1_id ASC,product2_id ASC;