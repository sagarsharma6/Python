#Ques 1
a=input("Enter string1: ")
b=input("Enter string2: ")
c=input("Enter string3: ")
my_list=[a,b,c]
print(my_list)

#Ques 2
my_list.extend(['google','apple','facebook','microsoft','tesla'])
print(my_list)

#Ques 3
my_list2=[1,2,3,1,4,2,5]
print("Count of obj 1: ",my_list2.count(1))

#Ques 4
my_list3=[5,4,3,2,1]
my_list3.sort()
print(my_list3)

#Ques 5
list1=[1,3,5,7]
list2=[2,4,6,8]
mylist=[]
mylist.extend(list1)
mylist.extend(list2)
mylist.sort()
print(mylist)

#Ques 6
#Implementation of stack using list
print("Implementation of stack using list: ")
list=[]
top=-1         #initilize top with -1
max_index=4   #lets assume max size of list is 5
option=1
while(option!=0):
    print("Enter 1 to push, 2 to pop, 3 to display, 0 to exit: ")
    option=int(input())
    if(option==1):
        if(top>=max_index):
            print("Overflow")
        else:
            top=top+1
            ele=int(input("Enter element: "))
            list.append(ele)
            print("Element inserted")
    elif(option==2):
        if(top==-1):
            print("Underflow")
        else:
            top=top-1
            print("Element popped")
    elif(option==3):
        if(top==-1):
            print("Empty Stack")
        else:
            print(list[top])                             #Since it is FILO so it will print the element present at top of stack
    elif(option==0):
        option=0
    else:
        print("Invalid input,try again")
        
#Implementation of queue using lsit
print("Implementation of queue using list: ")
list=[]
front=-1
rear=-1       
max=5   #lets assume max size of list is 5
option=1
while(option!=0):
    print("Enter 1 to enqueue, 2 to dequeue, 3 to display, 0 to exit: ")
    option=int(input())
    if(option==1):
        if(rear==max-1):
            print("Overflow")
        elif(rear==-1 and front==-1):
            rear=rear+1
            front=front+1
            ele=int(input("Enter element: "))
            list.append(ele)
            print("Element inserted")
        else:
            rear=rear+1
            ele=int(input("Enter element: "))
            list.append(ele)
            print("Element inserted") 
    elif(option==2):
        if(rear==-1 and front==-1):
            print("Underflow")
        elif(rear==front):
            rear=-1
            front=-1
            print("Element popped")
        else:
            front=front+1
            print("Element popped")
    elif(option==3):
        if(rear==-1 and front==-1):
            print("Empty Queue")
        else:
            print(list[front])                   #Since it is FIFO so it will print the element present which came first in queue
    elif(option==0):
        option=0
    else:
        print("Invalid input,try again")

#Optional question
#Ques 1
my_list=[2,3,1,5,6,4,7,8,9]
even_count=0
odd_count=0
for i in my_list:
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Count of even no:",even_count,"Count of odd no:",odd_count)
