WITH cte AS (
    SELECT person_name, turn, 
           SUM(weight) OVER (ORDER BY turn) AS running_total
    FROM Queue
)
SELECT person_name
FROM cte
WHERE running_total <= 1000
ORDER BY turn DESC
LIMIT 1;
