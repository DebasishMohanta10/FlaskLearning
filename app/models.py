import psycopg2
import os
CONNECTION_PARAMETERS = {
    'dbname': os.environ.get('DBNAME'),
    'user': os.environ.get('USER'),
    'password': os.environ.get('PASS') 
}

# with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
#     print(conn.get_dsn_parameters())
def removeTask(id):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         DELETE FROM task WHERE id=%(uid)s;
                         """,{"uid":id})
            return True


def getAllTodos():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM task ORDER BY id DESC;")
            result = curs.fetchall()
            return result
# print(getAllTodos())

def addTaskData(name,desc,deadline):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute(
    """
    INSERT INTO task(name,description,end_date)
        VALUES (%(task_name)s,%(desc)s,%(deadline)s)
    """,{"task_name": name,"desc":desc,"deadline": deadline}
            )
            return True

def searchTask(term):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute("""
                         SELECT * FROM task WHERE name ILIKE %s OR description ILIKE %s
                         """,('%'+term+'%','%'+term+'%'))
            result = curs.fetchall()
            return result
