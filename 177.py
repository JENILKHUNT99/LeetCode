#MySql:
"""
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set N=N-1;
  RETURN (
      # Write your MySQL query statement below.
    Select distinct salary from Employee order by salary desc limit 1 offset N
  );
END
"""
#Python:(Pandas)
'''
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    Unique_Salarys=employee['salary'].drop_duplicates()
    Sorted_Salarys=Unique_Salarys.sort_values(ascending=False)
    if N > len(Sorted_Salarys) or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    return pd.DataFrame({f'getNthHighestSalary({N})':[Sorted_Salarys.iloc[N-1]]})
'''