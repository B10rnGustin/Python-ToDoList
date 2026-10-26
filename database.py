import sqlite3

connection = sqlite3.connect("tasks.db")

cursor = connection.cursor()

command1 = """
CREATE TABLE IF NOT EXISTS tasks (
    Id INTEGER PRIMARY KEY, 
    Titel TEXT, 
    Aanmaakdatum TEXT, 
    Startdatum TEXT, 
    Einddatum TEXT, 
    Status TEXT, 
    Opmerking TEXT
)
"""

cursor.execute(command1)
connection.commit()

def get_all_tasks():
    def get_all_tasks():
        sql_opdracht = """
            SELECT *
            FROM tasks
            WHERE Status IS NULL OR Status != ?
        """
        cursor.execute(sql_opdracht, ("Done",))
        return cursor.fetchall()

def get_task_by_id(task_id):
    sql_opdracht = "SELECT * FROM tasks WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_id,))
    return cursor.fetchone()

def update_task_title(task_id, new_title):
    sql_opdracht = "UPDATE tasks SET Titel = ? WHERE Id = ?"
    cursor.execute(sql_opdracht, (new_title, task_id))
    connection.commit()

    return cursor.rowcount > 0

def update_task_status(task_id, new_status):
    sql_opdracht = "UPDATE tasks SET Status = ? WHERE Id = ?"
    cursor.execute(sql_opdracht, (new_status, task_id))
    connection.commit()

    return cursor.rowcount > 0

def update_task_einddatum(task_id, new_einddatum):
    sql_opdracht = "UPDATE tasks SET Einddatum = ? WHERE Id = ?"
    cursor.execute(sql_opdracht, (new_einddatum, task_id))
    connection.commit()

    return cursor.rowcount > 0

def replace_remark(task_id, nieuwe_opmerking):
    sql_opdracht = "UPDATE tasks SET Opmerking = ? WHERE Id = ?"
    cursor.execute(sql_opdracht, (nieuwe_opmerking, task_id))
    connection.commit()

    return cursor.rowcount > 0

def add_remark(task_id, extra_opmerking):

    sql_opdracht = "SELECT Opmerking FROM tasks WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_id,))
    resultaat = cursor.fetchone()

    if resultaat is None:
        return False

    huidige_opmerking = resultaat[0] or ""

    if huidige_opmerking:
        nieuwe_opmerking = huidige_opmerking + "\n" + extra_opmerking
    else:
        nieuwe_opmerking = extra_opmerking

    sql_opdracht = "UPDATE tasks SET Opmerking = ? WHERE Id = ?"
    cursor.execute(sql_opdracht, (nieuwe_opmerking, task_id))
    connection.commit()

    return True

def remove_remark(task_id):
    sql_opdracht = "UPDATE tasks SET Opmerking = '' WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_id,))
    connection.commit()
    return cursor.rowcount > 0

def delete_task(task_id):
    sql_opdracht = "DELETE FROM tasks WHERE Id = ?"
    cursor.execute(sql_opdracht, (task_id,))
    connection.commit()

    if cursor.rowcount == 0:
        return False

    return True

