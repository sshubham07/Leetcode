WITH cte AS (
    SELECT *, 
           RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS rnk 
    FROM Delivery
),
cte2 AS (
    SELECT * 
    FROM cte 
    WHERE rnk = 1
),
cte3 AS (
    SELECT 
        COUNT(CASE WHEN order_date = customer_pref_delivery_date THEN 1 END) AS imm, 
        COUNT(CASE WHEN order_date != customer_pref_delivery_date THEN 1 END) AS delay
    FROM cte2
)
SELECT ROUND(imm / (imm + delay) * 100, 2) AS immediate_percentage 
FROM cte3;
