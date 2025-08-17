# Write your MySQL query statement below
with cte as
(
    select book_id, count(CASE WHEN return_date is  NULL THEN 1 ELSE NULL END) as total from borrowing_records group by book_id
)
select b.book_id, b.title,b.author,b.genre,b.publication_year,b.total_copies as current_borrowers from library_books b join cte c on b.book_id=c.book_id and c.total=b.total_copies ORDER BY b.total_copies DESC,b.title;