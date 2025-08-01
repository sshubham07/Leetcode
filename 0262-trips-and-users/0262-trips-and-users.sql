WITH Total AS (
    SELECT 
        request_at, 
        COUNT(*) AS total_num
    FROM Trips
    WHERE 
        client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
        AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
        AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY request_at
),
Cancelled AS (
    SELECT 
        request_at, 
        COUNT(*) AS cancel_num
    FROM Trips
    WHERE 
        client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
        AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
        AND status IN ('cancelled_by_driver', 'cancelled_by_client')
        AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY request_at
)

SELECT 
    t.request_at AS Day,
    ROUND(IFNULL(c.cancel_num, 0) / t.total_num, 2) AS "Cancellation Rate"
FROM Total t
LEFT JOIN Cancelled c
ON t.request_at = c.request_at;
