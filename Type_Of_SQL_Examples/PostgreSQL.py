
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="database_name",
    user="user_name",
    password="password"
)

if conn.status == psycopg2.extensions.STATUS_READY:
    print("PostgreSQL is connected to the database.")

cursor = conn.cursor()

table_query = "CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255))"
cursor.execute(table_query)

insert_query = "INSERT INTO students (name, surname) VALUES (%s, %s)"
values = ("Alex", "Cheery")
cursor.execute(insert_query, values)

update_query = "UPDATE students SET name = %s WHERE id = %s"
values = ("Lilly", 1)
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
