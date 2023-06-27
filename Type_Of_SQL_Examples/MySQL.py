
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="user_name",
  password="password",
  database="database_name"
)

if conn.is_connected():
  print("MySQL is connected to the database.")

cursor = conn.cursor()

table_query = "CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255))"
cursor.execute(table_query)

insert_query = "INSERT INTO students (name, surname) VALUES (%s, %s)"
values = ("Anthony", "Price")
cursor.execute(insert_query, values)

update_query = "UPDATE students SET name = %s WHERE id = %s"
values = ("Robert", 1)
cursor.execute(update_query, values)

delete_query = "DELETE FROM students WHERE id = %s"
values = (1,)
cursor.execute(delete_query, values)

select_query = "SELECT * FROM students"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
  print(row)

conn.close()
