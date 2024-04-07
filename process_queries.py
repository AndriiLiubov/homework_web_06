from connect import create_connection
from pprint import pprint as print


def get_query1(file):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query)
        print(cursor.fetchall())

def get_query2(file, subject_id):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (subject_id,))
        print(cursor.fetchall())

def get_query3(file, subject):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (subject,))
        print(cursor.fetchall())

def get_query4(file):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query)
        print(cursor.fetchall())

def get_query5(file):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query)
        print(cursor.fetchall())

def get_query6(file, group):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (group,))
        print(cursor.fetchall())

def get_query7(file, group, subject):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (group, subject,))
        print(cursor.fetchall())

def get_query8(file, name):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (name,))
        print(cursor.fetchall())

def get_query9(file, name):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (name,))
        print(cursor.fetchall())

def get_query10(file, stud_name, teach_name):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (stud_name, teach_name,))
        print(cursor.fetchall())

def get_query11(file, stud_name, teach_name):

    with create_connection() as conn:
        cursor = conn.cursor()
        with open(f"queries/{file}") as sql:
            select_query = sql.read()
        cursor.execute(select_query, (stud_name, teach_name,))
        print(cursor.fetchall())

if __name__ == "__main__":
    # get_query1("query_1.sql")
    # get_query2("query_2.sql", 5)
    # get_query3("query_3.sql", "Algebra")
    # get_query4("query_4.sql")
    # get_query5("query_5.sql")
    # get_query6("query_6.sql", "Group C")
    # get_query7("query_7.sql", "Group B", "Algebra")
    # get_query8("query_8.sql", "Jennifer Watson")
    # get_query9("query_9.sql", "Aaron Sanchez")
    # get_query10("query_10.sql", "Jenna Taylor", "Stephanie Maddox")
    get_query11("query_11.sql", "Jenna Taylor", "Stephanie Maddox")