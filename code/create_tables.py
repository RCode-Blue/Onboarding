import sqlite3
import datetime
# from datetime import datetime

# TABLE CREATION
# ==============
connection = sqlite3.connect('database.db')
cursor = connection.cursor()


# users table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS users "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "name string, "
create_table += "job_title string, "
create_table += "team string)"

cursor.execute(create_table)
#endregion


# tasks table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS tasks "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "task_name string, "
create_table += "task_description text, "
create_table += "completed boolean, "
create_table += "completion_date text, "
create_table += "checked_off_by integer, "
create_table += "instructor_id integer, "
create_table += "task_notes text)"

cursor.execute(create_table)
#endregion


# positions table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS positions "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "template_id integer, "
create_table += "task_id integer, "
create_table += "position_no integer)"

cursor.execute(create_table)
#endregion


# templates table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS templates "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "template_name string, "
create_table += "description string)"

cursor.execute(create_table)
#endregion


# sets table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS sets "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "template_id integer, "
create_table += "description string, "
create_table += "city string, "
create_table += "start_date string, "
create_table += "employee_id integer, "
create_table += "manager_id integer, "
create_table += "buddy_id integer) "

cursor.execute(create_table)
#endregion


# sequences table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS sequences "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "set_id integer, "
create_table += "task_description string, "
create_table += "completed boolean, "
create_table += "completion_date string, "
create_table += "checked_off_by integer, "
create_table += "instructor_id integer, "
create_table += "task_notes string)"

cursor.execute(create_table)
#endregion






# **************************** Data ****************************


# Data: users table ------------------------------------
#region
SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Sophia Muntz', 'Senior Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Jett Allardyce', 'Senior Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Alica Ramsbotham', 'Senior Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Patrick Schlunke', 'Senior Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Austin Ashcroft', 'Senior Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Rebecca Ramsay', 'Senior Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Grace Michell', 'Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Logan Henn', 'Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Rory Clare', 'Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Maddison O''Brien', 'Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('John Mathew', 'Advisor', 'Melbourne')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Tyler Holland', 'Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Patrick Gilchrist', 'Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Zoe Ibbott', 'Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Lucy Mulga', 'Advisor', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Skye Kossak', 'Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Mackenzie Jeffrey', 'Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Cody Taubman', 'Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Matilda Holyman', 'Advisor', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Patrick Blakeney', 'Finance Manager', 'Brisbane')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Sienna Grant', 'IT Manager', 'Sydney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Bilbo Baggins', 'Uncle', 'The Shire')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Obi-Wan Kenobi', 'Jedi Master', 'Coruscant')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Frodo Baggins', 'Ring-Bearer', 'The Shire')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Luke Skywalker', 'Jedi', 'Tattooine')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Samwise Gamgee', 'Gardener', 'The Shire')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(name, job_title, team) VALUES"
SQLExecute += "('Chewbacca', 'Wookie', 'Kashyyyk')"
cursor.execute(SQLExecute)
#endregion


# Data: tasks table ------------------------------------
#region
# date format: yyyy-mm-dd
SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Complete and return signed forms', 'AA001', 2, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks "
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Collect computer log-in details', 'AA002', 21, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks "
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Access to Xero (Payroll System)', 'AA003', 21, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Access Slack and CatsOne', 'AA004', 21, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Develop your personal pitch and CareerTrackers pitch', 'AA005', 2, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Learn good vs bad recruitment', 'AA006', 3, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Gain an understanding of Student Suitability guidelines', 'AA007', 3, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks "
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Learn about the salary sacrificing opportunities', 'AA008', 20, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Complete Facebook Training and create your own profile', 'AA009', 4, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Participate in an Interview Preparation Training Workshop', 'AA010', 4, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Learn the travel approval process and where to go to access forms', 'AA011', 3, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Introduction to your state office', 'AA012', 5, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Observe student advisors undertake Monthly Meetings', 'AA013', 5, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Complete a one month progress check-in with your manager', 'AA014', 5, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Draft student CVs and gain feedback to ensure they met the standards of the program', 'AA015', 5, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Discuss a transition plan for you to begin taking on contact with corporate partners', 'AA016', 6, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Deliver Program Orientation Workshops and one-on-one', 'AA017', 6, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Interview three leaders within CareerTrackers to learn about their journey in the organisation', 'AA018', 6, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Take ring to Mordor', 'LL001', 22, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Celebrate 111st birthday', 'LL002', 22, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Meet at the Prancing Pony', 'LL003', 22, 'Change name to Underhill')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Form a fellowship', 'LL004', 22, 'Be careful of Boromir')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Go to Jedha', 'SS001', 23, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Beam plans from Scarif', 'SS002', 23, 'Callsign is Rogue One')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Hide plans in Droid', 'SS003', 23, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO tasks"
SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
SQLExecute += "('Drop bomb in thermal exhaust', 'SS004', 23, 'Use the Force')"
cursor.execute(SQLExecute)
#endregion


# Data: positions table ------------------------------------
#region
# Sydney
SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 1, 1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 2, 2)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 3, 3)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 4, 4)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 5, 5)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 6, 6)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 7, 7)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 8, 8)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(1, 9, 9)"
cursor.execute(SQLExecute)



# Melbourne
SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 10, 1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 11, 2)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 12, 3)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 13, 4)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 14, 5)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 15, 6)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 16, 7)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 17, 8)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 18, 9)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(2, 3, 10)"
cursor.execute(SQLExecute)



# Brisbane
SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 1, 1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 3, 2)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 5, 3)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 7, 4)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 9, 5)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 11, 6)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 13, 7)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 15, 8)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 17, 9)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 10, 10)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(3, 12, 11)"
cursor.execute(SQLExecute)



# Middle-Earth
SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(5, 19, 4)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(5, 21, 2)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(5, 20, 1)"
cursor.execute(SQLExecute)



# Rebel Alliance
SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(6, 23, 1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO positions"
SQLExecute += "(template_id, task_id, position_no) VALUES"
SQLExecute += "(6, 25, 3)"
cursor.execute(SQLExecute)

#endregion


# Data: templates table ------------------------------------
#region
SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Sydney Team Onboarding', 'Onboarding tasks for Sydney Student Advisors')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Melbourne Team Onboarding', 'Onboarding tasks for Melbourne Student Advisors')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Brisbane Team Onboarding', 'Onboarding tasks for Brisbane Student Advisors')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Perth Team Onboarding', 'Onboarding tasks for Perth Student Advisors')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Ring-Bearer Tasks', 'There and back again')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO templates"
SQLExecute += "(template_name, description) VALUES"
SQLExecute += "('Jedi Training', 'How to destroy a Death Star')"
cursor.execute(SQLExecute)
#endregion


# Data: sets table ------------------------------------
#region
SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(1, 'Sydney Onboarding for Tyler Holland', 'Sydney', '01-02-2019', 12, 1, 14)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(1, 'Sydney Onboarding for Patrick Gilchrist', 'Sydney', '02-03-2019', 13, 2, 14)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(2, 'Melbourne Onboarding for Grace Mitchell', 'Melbourne', '22-02-2019', 7, 3, 10)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(2, 'Melbourne Onboarding for Logan Henn', 'Melbourne', '22-02-2019', 8, 3, 9)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(3, 'Brisbane Onboarding for Skye Kossak', 'Brisbane', '29-02-2019', 16, 5, 20)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(3, 'Brisbane Onboarding for Mackenzie Jeffrey', 'Brisbane', '21-01-2019', 17, 5, 19)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(5, 'Ring-bearer quest for Bilbo Baggins', 'Middle-Earth', '21-01-2019', 24, 22, 26)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id) VALUES"
SQLExecute += "(6, 'Luke''s Jedi training checklist', 'Tattooine', '21-01-2019', 25, 23, 27)"
cursor.execute(SQLExecute)
#endregion


# Data: sequences table ------------------------------------
#region
SQLExecute = "INSERT INTO sequences "
SQLExecute += "(set_id) VALUES"
SQLExecute += "(1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sequences "
SQLExecute += "(set_id) VALUES"
SQLExecute += "(3)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sequences "
SQLExecute += "(set_id) VALUES"
SQLExecute += "(5)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sequences "
SQLExecute += "(set_id) VALUES"
SQLExecute += "(7)"


#endregion










connection.commit()
connection.close()
#endregion

