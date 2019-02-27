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
create_table += "google_id string, "
create_table += "email string, "
create_table += "name string, "
create_table += "given_name string, "
create_table += "family_name string, "
create_table += "picture string, "
create_table += "hd string, "
create_table += "token text, "
create_table += "created_at string)"

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
create_table += "buddy_id integer, "
create_table += "sequence_id integer)"

cursor.execute(create_table)
#endregion


# sequences table --------------------
#region
create_table = "CREATE TABLE IF NOT EXISTS sequences "
create_table += "(id INTEGER PRIMARY KEY, "
create_table += "set_id integer, "
create_table += "task_description string, "
create_table += "task_position integer, "
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
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('902347374856204501576', 'sophia.muntz@test.cx', 'Sophia Muntz', 'Sophia', 'Muntz')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('046107456723475023945', 'jett.allardyce@test.cx', 'Jett Allardyce', 'Jett', 'Allardyce')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('029345602964591609843', 'alica.ramsbotham@test.cx', 'Alica Ramsbotham', 'Alica', 'Ramsbotham')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('520885648849987983458', 'patrick.schlunke@test.cx', 'Patrick Schlunke', 'Patrick', 'Schlunke')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('234095872309485932485', 'austin.ashcroft@test.cx', 'Austin Ashcroft', 'Austin', 'Ashcroft')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('023453457609834650892', 'rebecca.ramsay@test.cx', 'Rebecca Ramsay', 'Rebecca', 'Ramsay')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('809659824659845098643', 'gracemichell@test.cx', 'Grace Michell', 'Grace', 'Michell')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('509823405986230498561', 'logan.henn@test.cx', 'Logan Henn', 'Logan', 'Henn')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('094856029846591846598', 'rory.clare@test.cx', 'Rory Clare', 'Rory', 'Clare')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('465289450243095826409', 'maddison.obrien@test.cx', 'Maddison O''Brien', 'Maddison', 'O''Brien')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('856238456298346509238', 'john.mathew@test.cx', 'John Mathew', 'John', 'Mathew')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('465029384650923465028', 'tyler.holland@test.cx', 'Tyler Holland', 'Tyler', 'Holland')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('345029834650928346501', 'patrick.gilchrist@test.cx', 'Patrick Gilchrist', 'Patrick', 'Gilchrist')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('984650986410018616546', 'zoe.ibbott@test.cx', 'Zoe Ibbott', 'Zoe', 'Ibbott')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('593465901834650345609', 'lucy.mulga@test.cx', 'Lucy Mulga', 'Lucy', 'Mulga')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('346519846501938465198', 'skye.kossak@test.cx', 'Skye Kossak', 'Skye', 'Kossak')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('098459385948444839458', 'mackenzie.jeffrey@test.cx', 'Mackenzie Jeffrey', 'Mackenzie', 'Jeffrey')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('234560236845984309582', 'cody.taubman@test.cx', 'Cody Taubman', 'Cody', 'Taubman')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('934805983465982348563', 'matilda.holyman@test.cx', 'Matilda Holyman', 'Matilda', 'Holyman')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('894650238465098263405', 'patrick.blakeney@test.cx', 'Patrick Blakeney', 'Patrick', 'Blakeney')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('862039485629834650924', 'sienna.grant@test.cx', 'Sienna Grant', 'Sienna', 'Grant')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('356285648689384933854', 'bilbo.baggins@test.cx', 'Bilbo Baggins', 'Bilbo', 'Baggins')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('584875847293452093485', 'obiwan.kenobi@test.cx', 'Obi-Wan Kenobi', 'Obi-Wan', 'Kenobi')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('014028650161456437180', 'frodo.baggins@test.cx', 'Frodo Baggins', 'Frodo', 'Baggins')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('145093620935239845934', 'luke.skywalker@test.cx', 'Luke Skywalker', 'Luke', 'Skywalker')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('598426592680298450892', 'samwise.gamgee@test.cx', 'Samwise Gamgee', 'Samwise', 'Gamgee')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO users"
SQLExecute += "(google_id, email, name, given_name, family_name) VALUES"
SQLExecute += "('745082450214305129856', 'chewbacca@test.cx', 'Chewbacca', 'Chewbacca', 'Chewbacca')"
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
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(1, 'Sydney Onboarding for Tyler Holland', 'Sydney', '01-02-2019', 12, 1, 14, 1)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(1, 'Sydney Onboarding for Patrick Gilchrist', 'Sydney', '02-03-2019', 13, 2, 14, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(2, 'Melbourne Onboarding for Grace Mitchell', 'Melbourne', '22-02-2019', 7, 3, 10, 2)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(2, 'Melbourne Onboarding for Logan Henn', 'Melbourne', '22-02-2019', 8, 3, 9, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(3, 'Brisbane Onboarding for Skye Kossak', 'Brisbane', '29-02-2019', 16, 5, 20, 3)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(3, 'Brisbane Onboarding for Mackenzie Jeffrey', 'Brisbane', '21-01-2019', 17, 5, 19, '')"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(5, 'Ring-bearer quest for Bilbo Baggins', 'Middle-Earth', '21-01-2019', 24, 22, 26, 4)"
cursor.execute(SQLExecute)

SQLExecute = "INSERT INTO sets"
SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, sequence_id) VALUES"
SQLExecute += "(6, 'Luke''s Jedi training checklist', 'Tattooine', '21-01-2019', 25, 23, 27, 5)"
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

