import psycopg2


# Postgres connection
#region
connection = psycopg2.connect(
  host="localhost",
  port="5432",
  database="onboarding",
  user="dev",
  password="password")
cursor = connection.cursor()
# print(cursor.description)
#endregion



# templates table
#region
drop_table = "DROP TABLE templates"
cursor.execute(drop_table)
#endregion


# tasks table
#region
drop_table = "DROP TABLE tasks"
cursor.execute(drop_table)
#endregion


# sets table
#region
drop_table = "DROP TABLE sets"
cursor.execute(drop_table)
#endregion


# sequences table
#region
drop_table = "DROP TABLE sequences"
cursor.execute(drop_table)
#endregion


# positions table
#region
drop_table = "DROP TABLE positions"
cursor.execute(drop_table)
#endregion


# users table
#region
drop_table = "DROP TABLE users"
cursor.execute(drop_table)
#endregion




connection.commit()
connection.close()