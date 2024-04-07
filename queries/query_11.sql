SELECT 
    ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
WHERE s.fullname = %s AND t.fullname = %s;
