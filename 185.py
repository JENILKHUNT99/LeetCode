#MySql:
'''
SELECT Department,Employee,Salary
FROM
    (SELECT
        D.name AS Department,
        E.name AS Employee,
        E.salary AS Salary,
        DENSE_RANK() OVER(PARTITION BY D.name ORDER BY E.salary DESC) AS RANKING
    FROM Employee AS E
    INNER JOIN Department AS D ON E.departmentId = D.id
    ) AS new_table
WHERE RANKING <=3
'''

#python(Pandas):
'''

'''
