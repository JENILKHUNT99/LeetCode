#MySql:
"""
SELECT 
    email 
FROM Person 
GROUP BY email 
HAVING COUNT( email ) > 1; 
"""
#Python:(Pandas)
'''
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    ans=person['email'].value_counts() [person['email'].value_counts()>1]
    return pd.DataFrame({'email':ans.index})
'''