SELECT 
    s.fullname AS student_name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.name = %s;