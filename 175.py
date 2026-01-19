#MySql:
"""
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
"""
#Python:(Pandas)
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = person.merge(address,on="personId",how="left")
    result=result[['firstName','lastName','city','state']]
    return result