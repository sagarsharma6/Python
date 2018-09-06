##All 4 questions done in single question below

import sqlite3 as sql
try:
    con=sql.connect('Students.db')                                                      #Establishing connection with database file
    cursor=con.cursor()
    query1='create table students(Name varchar(10), Marks int(3))'
    cursor.execute(query1)
    print("Table created.")
    lst=[]
    for i in range(10):
        print("Student",i,":")
        name=input("Enter name: ")
        marks=int(input("Enter marks(0 to 100): "))
        if(marks<0 or marks>100):                                                       #in case of invalid marks,data is skipped
            print("Invalid marks,skipping data of current student named",name)
            continue;
        tup=(name,marks)
        lst.append(tup)
    query2='insert into students(Name, Marks) values(?,?)'
    cursor.executemany(query2,lst)
    query3='select * from students'
    cursor.execute(query3)
    data=cursor.fetchall()
    print("Names of students who scored more than 80 marks: ")
    flag=0                                                                              #used to track if there is any student with marks greater than 80
    for row in data:
        if(row[1]>80):
            flag=1                                                                      #flag set to 1 if there is atleast one student with marks greater than 80                                                                          
            print(row[0])
    if(flag==0):                                                                        #if there is no student with marks greater than 80
        print("No students to display.")
    query4='delete from students'
    cursor.execute(query4)
    con.commit()
except sql.DatabaseError as e:
    if con:
        con.rollback()
        print("Error occured: ",e)
finally:
    if(cursor):
        cursor.close()
    if(con):
        con.close()
    print("Database closed.")
