# Write your MySQL query statement below
with cte as
(
    select u.name, count(m.user_id) as total, u.user_id from MovieRating m join  Users u on u.user_id = m.user_id group by u.user_id,u.name order by total DESC, u.name limit 1
),
cte3 as
(
    select * from MovieRating where DATE_FORMAT(created_at,"%Y-%m") = "2020-02"
),
cte2 as 
(
    select avg(mr.rating) as average, m.title from Movies m join cte3 mr on m.movie_id=mr.movie_id group by m.title order by average DESC, m.title limit 1
)

select name as results from cte
UNION ALL
select title as results from cte2;
-- select * from cte2;