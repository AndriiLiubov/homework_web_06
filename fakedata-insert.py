from faker import Faker
import random
from datetime import datetime, timedelta
from connect import create_connection

# Инициализация Faker
fake = Faker()

# Функция для создания случайной даты в определенном диапазоне
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Функция для заполнения таблицы групп случайными данными
def populate_groups(conn):
    groups = ["Group A", "Group B", "Group C"]
    with conn.cursor() as cursor:
        for group_name in groups:
            cursor.execute("INSERT INTO groups (name) VALUES (%s)", (group_name,))
        conn.commit()

# Функция для заполнения таблицы студентов случайными данными
def populate_students(conn, num_students):
    with conn.cursor() as cursor:
        for _ in range(num_students):
            fullname = fake.name()
            group_id = random.randint(1, 3)
            cursor.execute("INSERT INTO students (fullname, group_id) VALUES (%s, %s)", (fullname, group_id))
        conn.commit()

# Функция для заполнения таблицы преподавателей случайными данными
def populate_teachers(conn, num_teachers):
    with conn.cursor() as cursor:
        for _ in range(num_teachers):
            fullname = fake.name()
            cursor.execute("INSERT INTO teachers (fullname) VALUES (%s)", (fullname,))
        conn.commit()

# Функция для заполнения таблицы предметов случайными данными
def populate_subjects(conn, num_subjects):
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "History", "Literature", "Geography", "English", "Geometry", "Algebra", "Drawing"]
    with conn.cursor() as cursor:
        for _ in range(num_subjects):
            name = random.choice(subjects)
            teacher_id = random.randint(1, 3)
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (name, teacher_id))
        conn.commit()

# Функция для заполнения таблицы оценок случайными данными
def populate_grades(conn, num_grades):
    start_date = datetime(2023, 9, 1)
    end_date = datetime.now()
    with conn.cursor() as cursor:
        for _ in range(num_grades):
            student_id = random.randint(1, 50)  
            subject_id = random.randint(1, 8)  
            grade = random.randint(0, 100)  
            grade_date = random_date(start_date, end_date)
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)",
                           (student_id, subject_id, grade, grade_date))
        conn.commit()

if __name__ == "__main__":
    with create_connection() as conn:
        populate_groups(conn)
        populate_students(conn, 50) 
        populate_teachers(conn, 5)   
        populate_subjects(conn, 8)   
        populate_grades(conn, 100)   
