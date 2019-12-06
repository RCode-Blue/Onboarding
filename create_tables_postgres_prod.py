import os
import psycopg2
from datetime import datetime
from settings.dev_config import DevConfig

# TABLE CREATION
# ==============

# sqlite connection
#region
# connection = sqlite3.connect("database.db")
# cursor = connection.cursor()
#endregion

# Postgres connection
#region
connection = psycopg2.connect(
  host=DevConfig.POSTGRES["host"],
  port=DevConfig.POSTGRES["port"],
  database=DevConfig.POSTGRES["db"],
  user=DevConfig.POSTGRES["user"],
  password=DevConfig.POSTGRES["pw"])

# cursor = connection.cursor()
#endregion

# db_version = cursor.fetchone()
# print(db_version)

def create_tables():
  cursor = connection.cursor()
  # users table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS users "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "google_id VARCHAR, "
  create_table += "email VARCHAR, "
  create_table += "given_name VARCHAR, "
  create_table += "family_name VARCHAR, "
  create_table += "picture VARCHAR, "
  create_table += "hd VARCHAR, "
  create_table += "token VARCHAR, "
  create_table += "created_at DATE)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


  # tasks table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS tasks "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "task_name VARCHAR, "
  create_table += "task_description TEXT, "
  create_table += "completed BOOLEAN, "
  create_table += "completion_date TEXT, "
  create_table += "checked_off_by INTEGER, "
  create_table += "instructor_id INTEGER, "
  create_table += "task_notes TEXT)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


  # positions table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS positions "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "template_id INTEGER, "
  create_table += "task_id INTEGER, "
  create_table += "position_no INTEGER)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


  # templates table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS templates "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "template_name TEXT, "
  create_table += "description TEXT)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


  # sets table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS sets "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "template_id INTEGER, "
  create_table += "description TEXT, "
  create_table += "city TEXT, "
  create_table += "start_date DATE, "
  create_table += "employee_id INTEGER, "
  create_table += "manager_id INTEGER, "
  create_table += "buddy_id INTEGER, "
  create_table += "allocated BOOLEAN)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


  # sequences table --------------------
  #region
  create_table = "CREATE TABLE IF NOT EXISTS sequences "
  create_table += "(id SERIAL PRIMARY KEY, "
  create_table += "set_id INTEGER, "
  create_table += "task_description TEXT, "
  create_table += "task_position INTEGER, "
  create_table += "completed BOOLEAN, "
  create_table += "completion_date DATE, "
  create_table += "checked_off_by INTEGER, "
  create_table += "instructor_id INTEGER, "
  create_table += "task_notes TEXT)"

  cursor.execute(create_table)
  connection.commit()
  #endregion


# **************************** Data ****************************

def insert_data():
  cursor = connection.cursor()
  # Data: users table ------------------------------------
  #region
  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('902347374856204501576', 'sophia.muntz@test.cx', 'Sophia', 'Muntz')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('046107456723475023945', 'jett.allardyce@test.cx', 'Jett', 'Allardyce')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('029345602964591609843', 'alica.ramsbotham@test.cx', 'Alica', 'Ramsbotham')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('520885648849987983458', 'patrick.schlunke@test.cx', 'Patrick', 'Schlunke')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('234095872309485932485', 'austin.ashcroft@test.cx', 'Austin', 'Ashcroft')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('023453457609834650892', 'rebecca.ramsay@test.cx', 'Rebecca', 'Ramsay')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('809659824659845098643', 'gracemichell@test.cx', 'Grace', 'Michell')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('509823405986230498561', 'logan.henn@test.cx', 'Logan', 'Henn')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('094856029846591846598', 'rory.clare@test.cx', 'Rory', 'Clare')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('465289450243095826409', 'maddison.obrien@test.cx', 'Maddison', 'O""Brien')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('856238456298346509238', 'john.mathew@test.cx', 'John', 'Mathew')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('465029384650923465028', 'tyler.holland@test.cx', 'Tyler', 'Holland')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('345029834650928346501', 'patrick.gilchrist@test.cx', 'Patrick', 'Gilchrist')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('984650986410018616546', 'zoe.ibbott@test.cx', 'Zoe', 'Ibbott')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('593465901834650345609', 'lucy.mulga@test.cx', 'Lucy', 'Mulga')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('346519846501938465198', 'skye.kossak@test.cx', 'Skye', 'Kossak')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('098459385948444839458', 'mackenzie.jeffrey@test.cx', 'Mackenzie', 'Jeffrey')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('234560236845984309582', 'cody.taubman@test.cx', 'Cody', 'Taubman')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('934805983465982348563', 'matilda.holyman@test.cx', 'Matilda', 'Holyman')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('894650238465098263405', 'patrick.blakeney@test.cx', 'Patrick', 'Blakeney')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('862039485629834650924', 'sienna.grant@test.cx', 'Sienna', 'Grant')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('356285648689384933854', 'bilbo.baggins@test.cx', 'Bilbo', 'Baggins')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('584875847293452093485', 'obiwan.kenobi@test.cx', 'Obi-Wan', 'Kenobi')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('014028650161456437180', 'frodo.baggins@test.cx', 'Frodo', 'Baggins')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('145093620935239845934', 'luke.skywalker@test.cx', 'Luke', 'Skywalker')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('598426592680298450892', 'samwise.gamgee@test.cx', 'Samwise', 'Gamgee')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO users"
  SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  SQLExecute += "('745082450214305129856', 'chewbacca@test.cx', 'Chewbacca', '')"
  cursor.execute(SQLExecute)
  connection.commit()

  # SQLExecute = "INSERT INTO users"
  # SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  # SQLExecute += "('37658940061433522865', 'ZooomFoto@gmail.com', 'Zooom', 'Foto')"
  # cursor.execute(SQLExecute)
  # connection.commit()

  # SQLExecute = "INSERT INTO users"
  # SQLExecute += "(google_id, email, given_name, family_name) VALUES"
  # SQLExecute += "('735689400215367582886', '1000Hands@gmail.com', 'Thousand', 'Hands')"
  # cursor.execute(SQLExecute)
  # connection.commit()

  #endregion


  # Data: tasks table ------------------------------------
  #region
  # date format: yyyy-mm-dd
  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Complete and return signed forms', 'AA001', 2, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks "
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Collect computer log-in details', 'AA002', 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks "
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Access to Xero (Payroll System)', 'AA003', 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Access Slack and Database', 'AA004', 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Develop your personal pitch', 'AA005', 2, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Learn good vs bad recruitment', 'AA006', 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Gain an understanding of Suitability guidelines', 'AA007', 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks "
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Learn about the salary sacrificing opportunities', 'AA008', 20, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Complete Facebook Training and create your own profile', 'AA009', 4, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Participate in an Interview Preparation Training Workshop', 'AA010', 4, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Learn the travel approval process and where to go to access forms', 'AA011', 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Introduction to your state office', 'AA012', 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Observe student advisors undertake Monthly Meetings', 'AA013', 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Complete a one month progress check-in with your manager', 'AA014', 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Draft student CVs and gain feedback to ensure they met the standards of the program', 'AA015', 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Discuss a transition plan for you to begin taking on contact with corporate partners', 'AA016', 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Deliver Program Orientation Workshops and one-on-one', 'AA017', 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Interview three leaders within the organisation to learn about their journey in the organisation', 'AA018', 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Take ring to Mordor', 'LL001', 22, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Celebrate 111st birthday', 'LL002', 22, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Meet at the Prancing Pony', 'LL003', 22, 'Change name to Underhill')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Form a fellowship', 'LL004', 22, 'Be careful of Boromir')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Cross the bridge of Khazad-Dum', 'LL005', 22, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Attend the Council of Elrond', 'LL006', 22, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Go to Lothlorien', 'LL007', 22, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Go to Jedha', 'SS001', 23, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Beam plans from Scarif', 'SS002', 23, 'Callsign is Rogue One')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Hide plans in Droid', 'SS003', 23, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO tasks"
  SQLExecute += "(task_description, task_name, instructor_id, task_notes) VALUES"
  SQLExecute += "('Drop bomb in thermal exhaust', 'SS004', 23, 'Use the Force')"
  cursor.execute(SQLExecute)
  connection.commit()
  #endregion


  # Data: positions table ------------------------------------
  #region
  # Sydney
  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 1, 1)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 2, 2)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 3, 3)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 4, 4)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 5, 5)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 6, 6)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 7, 7)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 8, 8)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(1, 9, 9)"
  cursor.execute(SQLExecute)
  connection.commit()



  # Melbourne
  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 10, 1)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 11, 2)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 12, 3)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 13, 4)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 14, 5)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 15, 6)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 16, 7)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 17, 8)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 18, 9)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(2, 3, 10)"
  cursor.execute(SQLExecute)
  connection.commit()



  # Brisbane
  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 1, 1)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 3, 2)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 5, 3)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 7, 4)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 9, 5)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 11, 6)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 13, 7)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 15, 8)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 17, 9)"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 10, 10)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(3, 12, 11)"
  cursor.execute(SQLExecute)
  connection.commit()



  # Middle-Earth
  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(5, 19, 8)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(5, 21, 2)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(5, 20, 1)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(5, 22, 6)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(5, 23, 4)"
  cursor.execute(SQLExecute)
  connection.commit()




  # Rebel Alliance
  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(6, 23, 1)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO positions"
  SQLExecute += "(template_id, task_id, position_no) VALUES"
  SQLExecute += "(6, 25, 3)"
  cursor.execute(SQLExecute)
  connection.commit()

  #endregion


  # Data: templates table ------------------------------------
  #region
  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Sydney Team Onboarding', 'Onboarding tasks for Sydney Student Advisors')"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Melbourne Team Onboarding', 'Onboarding tasks for Melbourne Student Advisors')"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Brisbane Team Onboarding', 'Onboarding tasks for Brisbane Student Advisors')"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Perth Team Onboarding', 'Onboarding tasks for Perth Student Advisors')"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Ring-Bearer Tasks', 'There and back again')"
  cursor.execute(SQLExecute)
  #connection.commit()

  SQLExecute = "INSERT INTO templates"
  SQLExecute += "(template_name, description) VALUES"
  SQLExecute += "('Jedi Training', 'Jedi Academy Curriculum')"
  cursor.execute(SQLExecute)
  #connection.commit()
  #endregion


  # Data: sets table ------------------------------------
  #region
  SQLExecute = "INSERT INTO sets"
  SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, allocated) VALUES"
  SQLExecute += "(1, 'Sydney Onboarding for Tyler Holland', 'Sydney', '2019, 02, 01', 12, 1, 14, TRUE)"
  cursor.execute(SQLExecute)


  connection.commit()


  SQLExecute = "INSERT INTO sets"
  SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, allocated) VALUES"
  SQLExecute += "(1, 'Sydney Onboarding for Patrick Gilchrist', 'Sydney', '2019, 02, 03', 13, 2, 14, TRUE)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sets"
  SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, allocated) VALUES"
  SQLExecute += "(5, 'Ring-bearer quest for Bilbo Baggins', 'Middle-Earth', '2019, 01, 21', 24, 22, 26, FALSE)"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sets"
  SQLExecute += "(template_id, description, city, start_date, employee_id, manager_id, buddy_id, allocated) VALUES"
  SQLExecute += "(5, 'Ring-bearer quest for a Hobbit', 'Middle-Earth', '2019, 08, 21', 28, 22, 26, FALSE)"
  cursor.execute(SQLExecute)
  connection.commit()

  #endregion


  # Data: sequences table ------------------------------------
  #region

  # template 1
  #region
  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Complete and return signed forms', 1, 2, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Collect computer log-in details', 2, 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Access to Xero (Payroll System)', 3, 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Access Slack and CatsOne', 4, 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Develop your personal pitch and CareerTrackers pitch', 5, 2, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Learn good vs bad recruitment', 6, 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Gain an understanding of Student Suitability guidelines', 7, 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Learn about the salary sacrificing opportunities', 8, 20, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(1, 'Complete Facebook Training and create your own profile', 9, 4, '')"
  cursor.execute(SQLExecute)
  connection.commit()
  #endregion

  #template 2
  #region
  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Participate in an Interview Preparation Training Workshop', 1, 4, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Learn the travel approval process and where to go to access forms', 2, 3, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Introduction to your state office', 3, 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Observe student advisors undertake Monthly Meetings', 4, 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Complete a one month progress check-in with your manager', 5, 5, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Draft student CVs and gain feedback to ensure they met the standards of the program', 6, 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Discuss a transition plan for you to begin taking on contact with corporate partners', 7, 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Deliver Program Orientation Workshops and one-on-one', 8, 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Interview three leaders within CareerTrackers to learn about their journey in the organisation', 9, 6, '')"
  cursor.execute(SQLExecute)
  connection.commit()

  SQLExecute = "INSERT INTO sequences "
  SQLExecute += "(set_id, task_description, task_position, instructor_id, task_notes) VALUES"
  SQLExecute += "(2, 'Access to Xero (Payroll System)', 10, 21, '')"
  cursor.execute(SQLExecute)
  connection.commit()
  #endregion
  #endregion





  connection.commit()
  connection.close()
  #endregion


create_tables()
insert_data()



