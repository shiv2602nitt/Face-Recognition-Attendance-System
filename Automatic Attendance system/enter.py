import sqlite3

conn= sqlite3.connect('students.db')
print ("\nOpened database succesfully")
print("\nCreating Records....")

def insertOrUpdate(ide,name,roll,att):
    isRecordExist=0
    if int(ide) < 3:
        isRecordExist=1
    if isRecordExist==1:
        conn.execute("UPDATE STUDENTS SET NAME = ? WHERE ID = ?",(name, ide))
        conn.execute("UPDATE STUDENTS SET ROLL = ? WHERE ID = ?",(roll, ide))
        conn.execute("UPDATE STUDENTS SET ATTENDANCE = ? WHERE ID = ?",(att, ide))
    else:
        params = (ide, name, roll,att)                                               
        conn.execute("INSERT INTO STUDENTS VALUES(?, ?, ?,?)", params)
    conn.commit()
        
att=0
n=int(input ("How many records do you want to create ? "))
for i in range(0,n): 
    ide = input('Enter user id : ')
    name = input("Enter student's name : ")
    roll = input("Enter student's roll no. : ")
    insertOrUpdate(ide, name, roll,att)
    print (" ")
print ("\nRecords created successfully")
conn.close()
