#MySql:
"""
Select 
    Max(salary) as SecondHighestSalary 
from Employee 
where salary < (select max(salary) from Employee);
"""
#Python:(Pandas)
'''
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    Unique_Salarys=employee['salary'].drop_duplicates()
    second_highest=Unique_Salarys.nlargest(2).iloc[-1] if len(Unique_Salarys)>=2 else None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    return pd.DataFrame({'SecondHighestSalary':[second_highest]})
'''