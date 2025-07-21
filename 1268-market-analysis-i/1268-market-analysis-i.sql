# Write your MySQL query statement below
with cte as(select u.user_id as buyer_id, u.join_date,o.order_id from Users u left join Orders o on u.user_id=o.buyer_id and Year(o.order_date)="2019")
select buyer_id, join_date, count(order_id) as orders_in_2019  from cte group by buyer_id,join_date;