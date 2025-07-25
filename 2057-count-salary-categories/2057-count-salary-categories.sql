# Write your MySQL query statement below
with low as
(
    select "Low Salary" as category, count(case when income<20000 then 1 end) as accounts_count from Accounts
),
average as
(
    select "Average Salary" as category, count(case when income>=20000 and income<=50000 then 1 end) as accounts_count from Accounts
),
high as
(
    select "High Salary" as category, count(case when income>50000 then 1 end) as accounts_count from Accounts
)
select * from low
UNION ALL
select * from average
UNION ALL
select * from high;

