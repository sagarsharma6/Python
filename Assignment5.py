##Decision and flow control

#Ques 1

year=int(input("Enter year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")


#Ques 2

l=int(input("Enter length: "))
b=int(input("Enter breadth: "))
if(l==b):
    print("Square")      ##A square is also a rectangle.
else:
    print("Rectangle")


#Ques 3

first=int(input("Enter age of first preson: "))
second=int(input("Enter age of second preson: "))
third=int(input("Enter age of third preson: "))
if(first>second and first>third):
    print("Person 1 with age",first,"is oldest")
    if(second>third):
        print("Person 3 with age",third,"is youngest")
    else:
        print("Person 2 with age",second,"is youngest")
elif(second>third):
    print("Person 2 with age",second,"is oldest")
    if(first>third):
        print("Person 3 with age",third,"is youngest")
    else:
        print("Person 1 with age",first,"is youngest")
else:
    print("Person 3 with age",third,"is oldest")
    if(first>second):
        print("Person 2 with age",second,"is youngest")
    else:
        print("Person 1 with age",first,"is youngest")


#Ques 4

age=int(input("Enter age: "))
sex=input("Enter sex(M/F): ")
mar=input("Enter marital status(Y/N): ")
if(sex=='F'):
     print("She will work only in urban areas")
elif(sex=='M'):
    if(age>=20 and age<=40):
        print("He may work anywhere")
    elif(age>40 and age<=60):
        print("He will work only in urban areas")
else:
    print("ERROR")


#Ques 5

qty=int(input("Enter quantity: "))
cost=100
t_cost=qty*cost
if(t_cost>1000):
    t_cost-=t_cost/10
print("Total cost",t_cost)


##Loops

#Ques 1

l=[]
for i in range(10):
    num=input("Enter integer: ")
    l.append(num)
print(' '.join(l))


#Ques 2

while(1):
    print("This will print infinite times")


#Ques 3

list1=[int(input("Enter integer: ")) for i in range(5)]
list2=[i*i for i in list1]
print(list2)


#Ques 4

lst=[1,'abc',99.9,44.4,'xyz',2,3,'ijk',1.1]
lst_int=[]
lst_float=[]
lst_string=[]
for i in lst:
    if(type(i)==int):
        lst_int.append(i)
    elif(type(i)==float):
        lst_float.append(i)    
    else:
        lst_string.append(i)
print("Integer List",lst_int)
print("Float List",lst_float)
print("String List",lst_string)


#Ques 5:

lst_prime=[]
for i in range(1,101):
    for j in range(2,int(i/2)+1):
        if(i%j==0):
            break
    else:
        lst_prime.append(i)
print("List of prime numbers is",lst_prime)


#Ques 6

for i in range(4):
    for j in range(i+1):
        print("*",end='')
    print()


#Ques 7

lst=[input("Enter element: ") for i in range(5)]
search=input("Enter element to be searched: ")
for i in lst:
    if(search==i):
        lst.remove(i)
print("Updated list is",lst)
