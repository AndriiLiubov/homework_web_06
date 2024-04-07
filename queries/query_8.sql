SELECT 
    ROUND(AVG(grade), 2) AS average_grade
FROM teachers t
JOIN subjects subj ON t.id = subj.teacher_id
JOIN grades g ON subj.id = g.subject_id
WHERE t.fullname = %s;