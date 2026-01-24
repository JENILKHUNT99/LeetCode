#MySQL:
'''
SELECT 
    S.student_id,S.student_name,Su.subject_name,COUNT(E.student_id) AS `attended_exams`
FROM Students S
CROSS JOIN Subjects Su
LEFT JOIN Examinations E ON S.student_id=E.student_id AND E.subject_name=Su.subject_name
GROUP BY S.student_id,S.student_name,Su.subject_name
ORDER BY student_id,subject_name
'''
#python(Pandas):
'''

'''