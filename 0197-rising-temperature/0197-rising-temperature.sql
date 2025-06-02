# Write your MySQL query statement below
with temp as (select w2.id as id, w1.recordDate as d1, w2.recordDate as d2, w1.temperature as t1 , w2.temperature  as t2 from Weather w1 join Weather w2 on w1.recordDate + INTERVAL 1 DAY= w2.recordDate)
select id from temp where t2>t1;