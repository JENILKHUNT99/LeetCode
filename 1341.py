#MySQL:
'''
(SELECT 
    U.name AS results 
FROM Users AS U
JOIN MovieRating AS MR ON U.user_id=MR.user_id
GROUP BY U.name
ORDER BY COUNT(*) DESC , U.name 
LIMIT 1)
UNION ALL
(SELECT
    M.title AS results
FROM Movies M
JOIN MovieRating AS MR ON MR.movie_id=M.movie_id
WHERE MR.created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY M.title
ORDER BY AVG(MR.rating) DESC , M.title
LIMIT 1);
'''

#python(Pandas):
'''

'''

