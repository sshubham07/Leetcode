# Write your MySQL query statement below
with cte as
(
    select p.patient_id,p.patient_name,p.age,c.test_date,c.result, rank() over(partition by p.patient_id,c.result order by c.test_date) as rnk from patients p join covid_tests c on p.patient_id=c.patient_id and c.result="Positive"
),
positive as
(
    select * from cte where rnk =1
),
combined as 
(
    select p.patient_id,p.patient_name,p.age,p.test_date as first_positive_date, n.test_date as negative_date, rank() over(partition by n.patient_id order by n.test_date) as rnk from positive p join  covid_tests n on p.patient_id=n.patient_id and n.result="Negative" and p.test_date<n.test_date
),

final as
(
    select * from combined where rnk=1
)
select patient_id,patient_name, age, DATEDIFF(negative_date,first_positive_date) as recovery_time from final order by recovery_time,patient_name;