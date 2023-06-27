
import cx_Oracle

dsn_tns = cx_Oracle.makedsn('host', 'port', service_name='service_name')
conn = cx_Oracle.connect(user='user_name', password='password', dsn=dsn_tns)

if conn.version:
    print("Oracle, connect to the database.")

cursor = conn.cursor()

table_query = "CREATE TABLE students (id NUMBER PRIMARY KEY, name VARCHAR2(255), surname VARCHAR2(255))"
cursor.execute(table_query)

insert_query = "INSERT INTO students (id, name, surname) VALUES (:1, :2, :3)"
values = (1, "Johnny", "Cage")
cursor.execute(insert_query, values)
conn.commit()

update_query = "UPDATE students SET name = :1 WHERE id = :2"
values = ("David", 1)
cursor.execute(update_query, values)
conn.commit()

delete_query = "DELETE FROM students WHERE id = :1"
values = (1,)
cursor.execute(delete_query, values)
conn.commit()

select_query = "SELECT * FROM students"
cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
