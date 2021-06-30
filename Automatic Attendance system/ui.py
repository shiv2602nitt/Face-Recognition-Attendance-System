
print('---------------------------------------------------------------------------')
print('\t\tATTENDANCE SYSTEM USING FACIAL RECOGNITION ')
print('---------------------------------------------------------------------------')
print('\t\t NATIONAL INSTITUTE OF TECHNOLOGY, TIRUCHIRAPPALLI')
print('---------------------------------------------------------------------------')
print(" \n\n")
print("MENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT")
choice=int(input(">>>"))
ch=1
while ch!=0 and choice !=4:
    if choice==1:
        #import sqlpy as mark
        try:
            import sqlpy as mark
        except ImportError as error:
            print(error.__class__.__name__ + ": " + error.message)
        mark.first()
        choice=int(input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>"))
        continue
    elif choice==2:
    	#import sqlpy as mark1
        try:
            import sqlpy as mark1
        except ImportError as error:
            print(error.__class__.__name__ + ": " + error.message)
        mark1.displayDatabase()
        choice=int(input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>"))
        continue
    elif choice==3:
    	#import report as mark2
        try:
            import report as mark2
        except ImportError as error:
            print(error.__class__.__name__ + ": " + error.message)
        mark2.rep()
        print("\nReport generated successfully")
        choice=int(input("\nMENU\n(1)MARK ATTENDANCE\n(2)VIEW ATTENDANCE\n(3)GENERATE REPORT\n(4)QUIT\n\n>>>"))
        continue
    else:
        print("Invalid choice, please choose again")
        print("\n")
print("")
print(".")
import sqlite3
conn= sqlite3.connect('students.db')
#for i in range(0, 2):
cnd="UPDATE STUDENTS SET ATTENDANCE = 0 WHERE ID = 1 OR ID = 2 OR ID = 3"
cursor=conn.execute(cnd)
conn.commit()
conn.close()

