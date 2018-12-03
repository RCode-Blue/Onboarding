import sqlite3
import datetime
# from datetime import datetime

# TABLE CREATION
# ==============

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# tasks table ------------------------
create_table = "CREATE TABLE IF NOT EXISTS tasks "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "task_name string, "
create_table += "task_description text, "
create_table += "completed boolean, "
create_table += "completion_date datetime, "
create_table += "checked_off_by_id integer, "
create_table += "instructor_id integer)"

cursor.execute(create_table)



# sequence table
create_table = "CREATE TABLE IF NOT EXISTS sequences "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "sequence_name string, "
create_table += "sequence_description text)"

cursor.execute(create_table)




# position table --------------------
create_table = "CREATE TABLE IF NOT EXISTS position "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "position_name string, "
create_table += "task_id integer, "
create_table += "sequence_id integer, "
create_table += "sequence_no integer)"

cursor.execute(create_table)











# Data: Tasks table ------------------------------------


# date format: yyyy-mm-dd

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Complete and return signed forms', 'AA111', '', '', '', '')"
# cursor.execute("INSERT INTO tasks(task_description, completed, completion_date, checked_off_by_id, instructor_id) VALUES('task 1', True, '2017-11-22', 3, 5)")
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO tasks "
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Collect computer log-in details', 'AA222', '', '', '', '')"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Access Slack and CatsOne', 'AA333', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Develop your personal pitch and CareerTrackers pitch', 'AA444', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Learn good vs bad recruitment', 'AA555', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Gain an understanding of Student Suitability guidelines', 'AA666', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks "
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Learn about the salary sacrificing opportunities', 'AA777', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Complete Facebook Training and create your own profile', 'AA888', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Participate in an Interview Preparation Training Workshop', 'AA889', '', '', '', '')"
cursor.execute(SQLExecute)



SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, completed, completion_date, checked_off_by_id, instructor_id) VALUES"
SQLExecute += "('Learn the travel approval process and where to go to access forms', 'AA899', '', '', '', '')"
cursor.execute(SQLExecute)








# Data: Sequence table
SQLExecute = "INSERT INTO sequences "
SQLExecute += "(sequence_description, sequence_name) VALUES"
SQLExecute += "('Sydney Team Member Induction Program', 'SS')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sequences "
SQLExecute += "(sequence_description, sequence_name) VALUES"
SQLExecute += "('Melbourne Team Member Induction Program', 'MM')"
cursor.execute(SQLExecute)


# Data: Position table ------------------------

SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A1',1,1,1)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A2',3,1,2)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A3',5,1,3)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A4',7,1,4)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A5',9,1,5)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A6',2,1,6)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A7',4,1,7)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A8',6,1,8)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A9',2,2,1)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A10',4,2,2)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A11',3,2,3)"
cursor.execute(SQLExecute)


SQLExecute = "INSERT INTO position"
SQLExecute += "(position_name, task_id, sequence_id, sequence_no) VALUES"
SQLExecute += "('A12',1,2,4)"
cursor.execute(SQLExecute)



connection.commit()
connection.close()