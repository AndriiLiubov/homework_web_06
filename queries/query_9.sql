SELECT 
    subj.name AS course_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
WHERE s.fullname = %s;
