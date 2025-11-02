with cte as
(
    select c.name,o.id from Customers c left join Orders o on c.id=o.customerId
)
select name as Customers from cte where id is NULL;