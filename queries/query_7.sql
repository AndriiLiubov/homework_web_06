SELECT 
    s.fullname AS student_name, 
    g.grade AS grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
JOIN groups gr ON s.group_id = gr.id
WHERE gr.name = %s AND subj.name = %s;