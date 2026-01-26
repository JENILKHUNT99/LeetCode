#MySql:
'''
SELECT 
    T.id
FROM Weather T
CROSS JOIN Weather Y
WHERE 
    DATEDIFF(T.recordDate,Y.recordDate)=1 
    AND T.temperature > Y.temperature
'''
#python(Pandas):
'''

'''