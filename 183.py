#MySQL:
'''
SELECT C.name `Customers` 
FROM Customers C 
LEFT JOIN Orders O 
ON C.id=O.customerId WHERE O.id is null
'''
#Python:(Pandas)
'''
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    Ans=customers[~customers['id'].isin(orders['customerId'])]
    return pd.DataFrame({'Customers':Ans['name']})
'''