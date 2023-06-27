
import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=server_address;'
    'Database=database_name;'
    'UID=user_name;'
    'PWD=password;'
)

if conn.connected:
    print("SQL Server is connected to the database.")

cursor = conn.cursor()

table_query = "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255))"
cursor.execute(table_query)

insert_query = "INSERT INTO students (id, name, surname) VALUES (?, ?, ?)"
values = (1, "Giannis", "Rose")
cursor.execute(insert_query, values)
conn.commit()

update_query = "UPDATE students SET name = ? WHERE id = ?"
values = ("Justin", 1)
cursor.execute(update_query, values)
conn.commit()

delete_query = "DELETE FROM students WHERE id = ?"
values = (1,)
cursor.execute(delete_query, values)
conn.commit()

select_query = "SELECT * FROM students"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
