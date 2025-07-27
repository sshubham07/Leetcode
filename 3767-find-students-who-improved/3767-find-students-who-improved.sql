WITH cte1 AS (
    SELECT *
    FROM Scores s1
    WHERE STR_TO_DATE(exam_date, '%Y-%m-%d') = (
        SELECT MIN(STR_TO_DATE(exam_date, '%Y-%m-%d'))
        FROM Scores
        WHERE student_id = s1.student_id AND subject = s1.subject
    )
),
cte2 AS (
    SELECT *
    FROM Scores s2
    WHERE STR_TO_DATE(exam_date, '%Y-%m-%d') = (
        SELECT MAX(STR_TO_DATE(exam_date, '%Y-%m-%d'))
        FROM Scores
        WHERE student_id = s2.student_id AND subject = s2.subject
    )
)
SELECT 
    cte1.student_id,
    cte1.subject,
    cte1.score AS first_score,
    cte2.score AS latest_score
FROM cte1
JOIN cte2
  ON cte1.student_id = cte2.student_id AND cte1.subject = cte2.subject
WHERE cte2.score > cte1.score order by cte1.student_id,cte1.subject;
