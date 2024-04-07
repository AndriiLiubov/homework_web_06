SELECT 
    t.fullname AS teacher_name, 
    subj.name AS course_name
FROM teachers t
JOIN subjects subj ON t.id = subj.teacher_id;