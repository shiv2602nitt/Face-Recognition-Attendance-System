import sqlite3
conn=sqlite3.connect("students.db")

cmd="SELECT * FROM STUDENTS"
cursor=conn.execute(cmd)
for row in cursor:
    print(row)		 


conn.commit()
conn.close()
