#MySQL:
'''
SELECT 
    name
FROM Employee
WHERE id IN (
    SELECT managerId  
    FROM EMPLOYEE 
    GROUP BY managerId 
    HAVING COUNT(managerId) >=5)
'''
#python(Pandas):
'''

'''