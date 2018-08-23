flag=0
while(1):
    if(flag==0):
        gender=input("Enter gender(M/F): ")
        if(gender!='M' and gender!='F' and gender!='m' and gender!='f'):
            print("That's a new kind of gender,isn't that?")
            break
    flag=1
    name=input("Enter name: ")
    if(name.isalpha()):
        if(gender=='M' or gender=='m'):
            print("Hello",name,"Sir")
        else:
            print("Hello",name,"Mam")
    else:
        print("Try again with a valid name")
        continue
    age=input("Enter age: ")
    if(age.isdigit()):
        age=int(age)
        if(gender=='M' or gender=='m' and age>20):
            print("you are  able  to enroll for python fundamental course")
        elif(gender=='F' or gender=='f' and age>19):
            print("you are able to enroll for core java course")
        else:
            print("you are below age criteria,you can't enroll the course")
            break
    else:
        print("What kind of age is that..?")
    break
    
    
