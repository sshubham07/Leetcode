with cte as
(
    select customer_id, count(distinct product_key) as total from customer group by customer_id
)
-- select * from cte;
-- select count(*) from Product;
select customer_id from cte where total = (select count(*) from Product);