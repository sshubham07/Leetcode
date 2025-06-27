import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique = employee['salary'].dropna().drop_duplicates().sort_values(ascending=False)
    if len(unique) >= N and N>0:
        ans = unique.iloc[N-1]
    else:
        ans = None
    return pd.DataFrame({f'getNthHighestSalary({N})':[ans]})