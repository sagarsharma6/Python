#Ques 1

d={'1':'abc','2':'def','3':'ghi','4':'jkl'}
for key in d:
    print(key,d[key])


#Ques 2

dic={}
dic2={}
for i in range(3):
    name=input("Enter name of student: ")
    print("Student",name,":")
    for marks in range(3):
        s=input("Enter subject: ")
        m=int(input("Enter marks: "))
        dic2[s]=m
    dic[name]=dic2.copy()
    dic2.clear()
nam=input("Enter student name whose marks you want to display: ")
for i in dic.keys():
    if(nam==i):
        print(dic[nam])
        break
else:
    print("Name",nam,"not found")
