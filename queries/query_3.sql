SELECT
    g.name AS group_name, 
    ROUND(AVG(grade), 2) AS average_grade
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN grades gr ON s.id = gr.student_id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE subj.name = %s
GROUP BY g.name;
